""" CombatLog Models """

import logging
import os
import traceback

from core.models import BaseModel
from django.db import models, transaction
from django.dispatch import receiver
from ladder.models import Ladder, LadderEntry
from rest_framework.exceptions import APIException

import OSCR

from .metadata import Metadata

LOGGER = logging.getLogger("django")


class CombatLog(BaseModel):
    """CombatLog Model"""

    file = models.FileField(upload_to="uploads")

    metadata = models.ForeignKey(
        Metadata,
        on_delete=models.CASCADE,
        null=True,
    )

    def delete_file(self):
        """Delete the uploaded combat log"""
        if self.file:
            if os.path.exists(self.file.path):
                os.remove(self.file.path)

    def update_metadata(self):
        """Parse the Combat Log and create Metadata"""
        parser = OSCR.OSCR(self.file.path)
        parser.analyze_log_file()

        # Only look at the first combat for now.
        parser.shallow_combat_analysis(0)
        combat = parser.active_combat
        summary = parser.active_combat.player_dict

        # Check to see if map / difficulty combination exists in the ladder
        # table. if it does, iterate over each player to see if they have a
        # higher key. If any of them do, allow uploading of the log and
        # add/update players into the league table.

        ladders = Ladder.objects.filter(
            internal_name=combat.map,
            internal_difficulty=combat.difficulty,
        )

        if ladders.count() == 0:
            raise APIException(
                f"{combat.map} {combat.difficulty} is not a valid ladder"
            )

        added = False
        for full_name, player in summary.items():
            for ladder in ladders:
                queryset = LadderEntry.objects.filter(
                    ladder=ladder,
                    player=full_name,
                )
                if queryset.count() == 0:
                    LOGGER.info(
                        f"New Entry: {full_name}: {combat.map} ({combat.difficulty}) - {player.DPS} DPS"
                    )
                    LadderEntry.objects.create(
                        player=full_name,
                        data=player._asdict(),
                        combatlog=self,
                        ladder=ladder,
                    )
                    added = True
                elif queryset.filter(
                    **{f"data__{ladder.metric}__gt": getattr(player, ladder.metric)}
                ):
                    LOGGER.info(
                        f"Updated Entry: {full_name}: {combat.map} ({combat.difficulty}) - {player.DPS} DPS"
                    )
                    queryset.update(
                        player=full_name,
                        data=player._asdict(),
                        combatlog=self,
                        ladder=ladder,
                    )
                    added = True

        if not added:
            raise APIException("No entries were updated")

        with transaction.atomic():
            if self.metadata is None:
                self.metadata = Metadata(
                    map=combat.map,
                    difficulty=combat.difficulty,
                    summary=summary,
                )
                self.metadata.save()
            self.save()

    def __str__(self):
        return self.file.name


@receiver(models.signals.post_delete, sender=CombatLog)
def combat_log_post_delete(sender, instance, **kwargs):
    """
    Automatically Delete CombatLog file on model deletion.
    """

    if instance.metadata:
        instance.metadata.delete()
    instance.delete_file()


@receiver(models.signals.post_save, sender=CombatLog)
def combat_log_post_save(sender, instance, created, **kwargs):
    """
    Automatically Delete CombatLog file on model deletion.
    """

    if created:
        try:
            instance.update_metadata()
        except Exception as e:
            instance.delete()
            traceback.print_exc()
            raise APIException(f"Failed to update metadata: {e}")
