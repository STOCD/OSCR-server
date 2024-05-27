""" CombatLog Models """

import logging
import os
import tempfile
from pathlib import Path

import OSCR
from django.conf import settings
from django.db import models, transaction
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.exceptions import APIException

from core.models import BaseModel
from ladder.models import Ladder, LadderEntry

from .metadata import Metadata

LOGGER = logging.getLogger("django")


class CombatLog(BaseModel):
    """CombatLog Model"""

    metadata = models.ForeignKey(
        Metadata,
        on_delete=models.CASCADE,
        null=True,
    )

    name = models.TextField(null=True, default=None)
    youtube = models.TextField(null=True, default=None)

    def update_metadata_from_remote(self):
        """Updates Metadata from remote storage"""
        data = self.get_data()
        if data:
            self.update_metadata(data)

    def update_metadata_file(self, file):
        """Update Metadata from a file"""

        results = []

        parser = OSCR.OSCR(file.name)
        parser.analyze_log_file()

        # Only look at the first combat for now.
        parser.shallow_combat_analysis(0)
        combat = parser.active_combat

        players = {}
        for name, player in parser.active_combat.players.items():
            players[name] = player.__dict__

        players = sorted(
            players.items(),
            reverse=True,
            key=lambda player: player[1]["combat_time"],
        )

        if len(players) == 0:
            raise APIException("Combat log is empty")

        # Grab the highest combat_time. This is used to validate other players.
        # Player combat_time should be within 90% of the highest time.
        combat_time = players[0][1]["combat_time"] * 0.90

        # Check to see if map / difficulty combination exists in the ladder
        # table. if it does, iterate over each player to see if they have a
        # higher key. If any of them do, allow uploading of the log and
        # add/update players into the league table.

        # FIXME: This spams a lot of DateTimeField Variant... has received a
        #        naive datetime messages here. This is because there's no way
        #        to know the combat log's time zone purely from the combat log.
        #        Great job Cryptic.

        ladders = Ladder.objects.filter(
            internal_name=combat.map,
            internal_difficulty=combat.difficulty,
            variant__start_date__lte=combat.start_time,
            variant__end_date__gt=combat.end_time,
        )

        # Now need to apply exclusions
        adjusted_ladders = []
        for ladder in ladders:
            if ladder.is_space and ladder.variant.is_space_variant:
                if ladder.variant.exclude_space.filter(
                    start_date__lte=combat.start_time,
                    end_date__gt=combat.end_time,
                ).count():
                    continue
            elif not ladder.is_space and ladder.variant.is_ground_variant:
                if ladder.variant.exclude_ground.filter(
                    start_date__lte=combat.start_time,
                    end_date__gt=combat.end_time,
                ).count():
                    continue
            adjusted_ladders.append(ladder)
        ladders = adjusted_ladders

        if len(ladders) == 0:
            raise APIException(
                f"{combat.map} {combat.difficulty} at {combat.start_time} has no matching ladder"
            )

        for _, player in players:
            full_name = f"{player['name']}{player['handle']}"
            if player["combat_time"] < combat_time:
                results.append(
                    {
                        "name": full_name,
                        "updated": False,
                        "detail": f"{full_name}'s combat time was too low.",
                        "value": combat_time,
                    }
                )
                continue

            for ladder in ladders:
                if ladder.is_solo and len(players) != 1:
                    continue

                if ladder.manual_review_threshold and player.get(ladder.metric) > ladder.manual_review_threshold:
                    visible = False
                    manual_review = f", but result needs to be manually reviewed. Combat Log ID #{self.pk}"
                else:
                    visible = True
                    manual_review = ""

                queryset = LadderEntry.objects.filter(
                    ladder=ladder,
                    player=full_name,
                )
                if queryset.count() == 0:
                    result = {
                        "name": full_name,
                        "updated": True,
                        "detail": f"New entry for {full_name} on {ladder}{manual_review}",
                        "value": player.get(ladder.metric),
                    }
                    LadderEntry.objects.create(
                        player=full_name,
                        data=player,
                        combatlog=self,
                        ladder=ladder,
                        visible=visible,
                    )
                elif not queryset.filter(
                    **{f"data__{ladder.metric}__gte": player.get(ladder.metric)}
                ).count():
                    result = {
                        "name": full_name,
                        "updated": True,
                        "detail": f"Updated entry for {full_name} on {ladder}{manual_review}",
                        "value": player.get(ladder.metric),
                    }
                    queryset.update(
                        player=full_name,
                        data=player,
                        combatlog=self,
                        ladder=ladder,
                        visible=visible,
                    )
                else:
                    result = {
                        "name": full_name,
                        "updated": False,
                        "detail": f"No updates for {full_name} on {ladder}",
                        "value": player.get(ladder.metric),
                    }

                results.append(result)

        updated = 0
        for result in results:
            if result["updated"]:
                updated += 1

        if updated == 0:
            raise APIException("There are no new records in this combat log.")

        with transaction.atomic():
            if self.metadata is None:
                self.metadata = Metadata(
                    map=combat.map,
                    difficulty=combat.difficulty,
                    date_time=timezone.make_aware(combat.date_time),
                    summary=players,
                )
                self.metadata.save()
            self.save()

        # Delete any combat logs that do not have ladder entries
        CombatLog.objects.filter(ladderentry=None).delete()

        return results

    def update_metadata(self, data):
        """Parse the Combat Log and create Metadata"""

        with tempfile.NamedTemporaryFile() as file:
            file.write(data)
            file.flush()
            res = self.update_metadata_file(file)
            self.put_data(data)

        return res

    def get_data_upload_path(self):
        """Return the Path to the combat log data"""
        return os.path.join(settings.UPLOAD_ROOT, "combatlogs", f"{self.pk}.log")

    def get_data_download_path(self):
        """Return the Path to the combat log data"""
        return self.name

    def get_data(self):
        """Fetch the Combat Log data"""
        if self.get_data_download_path() is None:
            return b""
        with open(self.get_data_upload_path(), "rb") as file:
            return file.read()

    def put_data(self, data):
        """Store the Combat Log data"""
        parent = Path(self.get_data_upload_path()).parent
        if not os.path.exists(parent):
            os.makedirs(parent, exist_ok=True)

        with open(self.get_data_upload_path(), "wb") as file:
            file.write(data)
        self.name = self.get_data_upload_path()
        self.save()

    def delete_data(self):
        """Delete the Combat Log data"""
        if os.path.exists(self.get_data_upload_path()):
            os.remove(self.get_data_upload_path())

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

    if instance.get_data_download_path():
        instance.delete_data()
