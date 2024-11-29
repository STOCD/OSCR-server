"""CombatLog Models"""

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

    def get_data_from_row(self, row, keys):
        """Get an indidual row of data from the Tree"""
        ret = {}
        for idx in range(1, len(row)):
            ret[keys[idx]] = row[idx]
        return ret

    def enumerate_tree(self, name, node, keys, max_depth=1):
        """Get Player Data from a specific node in the Tree"""
        ret = {"name": name, "summary": {}, "breakdown": []}
        ret["summary"] = self.get_data_from_row(node.data, keys)
        if max_depth:
            for idx in range(node.child_count):
                source = node.get_child(idx)
                source_name = "".join(source.data[0])
                ret["breakdown"].append(
                    self.enumerate_tree(
                        source_name,
                        source,
                        keys,
                        max_depth=max_depth - 1,
                    )
                )
        ret["breakdown"] = sorted(
            ret["breakdown"],
            reverse=True,
            key=lambda data: data["summary"]["DPS"],
        )

        return ret

    def tree_to_dict(self, tree):
        """Contert OSCR's Tree class to a dictionary for easier use"""
        data = {"players": []}
        keys = list(tree.data)

        # Players
        players = tree.get_child(0)
        for idx in range(players.child_count):
            name = "".join(players.get_child(idx).data[0])
            data["players"].append(
                self.enumerate_tree(
                    name,
                    players.get_child(idx),
                    keys,
                )
            )
        data["players"] = sorted(
            data["players"],
            reverse=True,
            key=lambda data: data["summary"]["DPS"],
        )

        # TODO: Critters, but not necessary
        # critters = tree.get_child(1)

        return data

    def get_build(self, damage_out):
        """
        Return the 'build' from the damage out entry.
        This is a hack that will just return the top DPS ability.
        """
        if not len(damage_out):
            return "Unknown"
        return damage_out[0]["name"]

    def update_metadata_from_remote(self):
        """Updates Metadata from remote storage"""
        data = self.get_data()
        if data:
            self.update_metadata(data, force=True)

    def update_metadata_file(self, file, force=False):
        """Update Metadata from a file"""

        results = []

        parser = OSCR.OSCR(file.name)
        parser.analyze_log_file()

        # Only look at the first combat for now.
        dmg_out, _, _, _ = parser.full_combat_analysis(0)
        damage_out = self.tree_to_dict(dmg_out)
        combat = parser.active_combat

        players = {}
        for name, player in combat.players.items():
            players[name] = player.__dict__

        players = sorted(
            players.items(),
            reverse=True,
            key=lambda player: player[1]["combat_time"],
        )

        # Add the damage out to the player.
        for idx, player in enumerate(players):
            handle = f"{player[1]['name']}{player[1]['handle']}"
            for damage_out_player in damage_out["players"]:
                if damage_out_player["name"] == handle:
                    # Override Build with damage breakdown
                    players[idx][1]["build"] = self.get_build(
                        damage_out_player["breakdown"]
                    )
                    break

        if len(players) == 0:
            raise APIException("Combat log is empty")

        # TBD: We use 0.9 combat time until a better choice can be made.
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
        ) | Ladder.objects.filter(
            internal_name=combat.map,
            internal_difficulty=None,
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
                f"{combat.map} ({combat.difficulty} Difficulty) at {
                    combat.start_time} has no matching ladder"
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

                if (
                    ladder.manual_review_threshold
                    and player.get(ladder.metric) > ladder.manual_review_threshold
                ):
                    visible = False
                    manual_review = f", but result needs to be manually reviewed. Combat Log ID #{
                        self.pk}"
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

        # No not raise an exception here anymore - return the status indicating why no logs were updated.
        if updated == 0 and not force:
            return results

        with transaction.atomic():
            if self.metadata is None:
                self.metadata = Metadata(
                    map=combat.map,
                    difficulty=combat.difficulty,
                    date_time=timezone.make_aware(combat.date_time),
                    summary=players,
                    damage_out=damage_out,
                )
                self.metadata.save()
            else:
                self.metadata.summary = players
                self.metadata.damage_out = damage_out
                self.metadata.save()
                # Need to backtrack and update the ladder entries.
                for entry in self.ladderentry_set.all():
                    for _, player in players:
                        full_name = f"{player['name']}{player['handle']}"
                        if entry.player == full_name:
                            entry.data = player
                            entry.save()
                            break
            self.save()

        # Delete any combat logs that do not have ladder entries
        CombatLog.objects.filter(ladderentry=None).delete()

        return results

    def update_metadata(self, data, force=False):
        """Parse the Combat Log and create Metadata"""

        with tempfile.NamedTemporaryFile(delete=False) as file:
            file.write(data)
            file.flush()
            file.close()
            res = self.update_metadata_file(file, force)
            self.put_data(data)
            os.unlink(file.name)

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
