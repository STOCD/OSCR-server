""" CombatLog Models """

import logging
import tempfile

import OSCR
from core.models import BaseModel
from django.db import models, transaction
from django.dispatch import receiver
from django.utils import timezone
from ladder.models import Ladder, LadderEntry
from rest_framework.exceptions import APIException

from .metadata import Metadata

LOGGER = logging.getLogger("django")


class CombatLog(BaseModel):
    """CombatLog Model"""

    data = models.BinaryField(null=True, default=None)

    metadata = models.ForeignKey(
        Metadata,
        on_delete=models.CASCADE,
        null=True,
    )

    def update_metadata_file(self, file):
        """Update Metadata from a file"""

        results = []

        parser = OSCR.OSCR(file.name)
        parser.analyze_log_file()

        # Only look at the first combat for now.
        parser.shallow_combat_analysis(0)
        combat = parser.active_combat
        summary = sorted(
            parser.active_combat.player_dict.items(),
            reverse=True,
            key=lambda player: player[1].combat_time,
        )

        if len(summary) == 0:
            raise APIException("Combat log is empty")

        # Grab the highest combat_time. This is used to validate other players.
        # Player combat_time should be within 95% of the highest time.
        combat_time = summary[0][1].combat_time * 0.95

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

        for full_name, player in summary:
            if player.combat_time < combat_time:
                results.append(
                    {
                        "name": full_name,
                        "updated": False,
                        "detail": f"{full_name}'s combat time was too low.",
                    }
                )
                continue

            for ladder in ladders:
                queryset = LadderEntry.objects.filter(
                    ladder=ladder,
                    player=full_name,
                )
                if queryset.count() == 0:
                    result = {
                        "name": full_name,
                        "updated": True,
                        "detail": f"New entry for {full_name} on {ladder}",
                    }
                    LadderEntry.objects.create(
                        player=full_name,
                        data=player._asdict(),
                        combatlog=self,
                        ladder=ladder,
                    )
                elif not queryset.filter(
                    **{
                        f"data__{ladder.metric}__gte": getattr(
                            player, f"{ladder.metric}"
                        )
                    }
                ).count():
                    result = {
                        "name": full_name,
                        "updated": True,
                        "detail": f"Updated entry for {full_name} on {ladder}",
                    }
                    queryset.update(
                        player=full_name,
                        data=player._asdict(),
                        combatlog=self,
                        ladder=ladder,
                    )
                else:
                    result = {
                        "name": full_name,
                        "updated": False,
                        "detail": f"No updates for {full_name} on {ladder}",
                    }

                results.append(result)

        with transaction.atomic():
            if self.metadata is None:
                self.metadata = Metadata(
                    map=combat.map,
                    difficulty=combat.difficulty,
                    date_time=timezone.make_aware(combat.date_time),
                    summary=summary,
                )
                self.metadata.save()
            self.save()

        # Delete any combat logs that do not have ladder entries
        CombatLog.objects.filter(ladderentry=None).delete()

        return results

    def update_metadata(self):
        """Parse the Combat Log and create Metadata"""
        with tempfile.NamedTemporaryFile() as file:
            file.write(self.data)
            file.flush()
            return self.update_metadata_file(file)

    def __str__(self):
        if not self.metadata:
            return f"Combat Log without Metadata ({self.pk})"
        return f"{self.metadata.map} {self.metadata.difficulty}"


@receiver(models.signals.post_delete, sender=CombatLog)
def combat_log_post_delete(sender, instance, **kwargs):
    """
    Automatically Delete CombatLog file on model deletion.
    """

    if instance.metadata:
        instance.metadata.delete()
