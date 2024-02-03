""" CombatLog Models """

import logging
import os
import traceback

import OSCR
from core.models import BaseModel
from django.db import models, transaction
from django.dispatch import receiver
from ladder.models import Ladder, LadderEntry
from rest_framework.exceptions import APIException

from .metadata import Metadata

LOGGER = logging.getLogger("django")


def get_dict(player):
    """This is a hack because a player is not json serialziable."""
    return {
        "name": player.name,
        "is_player": player.isPlayer,
        "total_damage": player.totaldamage,
        "total_attacks": player.totalAttacks,
        "total_hull_damage": player.hulllDamage,
        "total_shield_damage": player.shieldDamage,
        "total_heal_instances": player.totalHealInstances,
        "total_crits": player.totalCrits,
        "total_heal_crits": player.totalHealCrits,
        "total_heals": player.totalHeals,
        "total_damage_taken": player.totalDamageTaken,
        "total_attacks_taken": player.totalAttacksTaken,
        "deaths": player.deaths,
        "max_one_hit": player.maxOneHit,
        "max_one_hit_weapon": player.maxOneHitWeapon,
        "max_one_heal": player.maxOneHeal,
        "max_one_heal_weapon": player.maxOneHealWeapon,
        "dps": player.DPS,
        "crith": player.crtH,
        "heal_crith": player.healCrtH,
        "start_time": str(player.startTime),
        "total_time": str(player.totalTime),
        "flanks": player.flanks,
        "misses": player.misses,
        "kills": player.kills,
        "runtime": str(player.runtime),
        "end_time": str(player.endTime),
        "accuracy": player.acc,
        "resist": player.resist,
        "hull_attacks": player.hullAttacks,
        "final_resist": player.finalresist,
        "percent_attacks": player.ATKSinPercentage,
        "percent_damage": player.dmgPercentage,
        "percent_damage_taken": player.percentageTaken,
        "percent_healed": player.percentageHealed,
        "attacks_per_minute": player.ATKSpMin,
        "hps": player.HPS,
    }


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
        parser = OSCR.parser()
        parser.readCombatShallow(self.file.path)
        summary = [get_dict(player) for player in parser.tableArray]

        # Check to see if map / difficulty combination exists in the ladder
        # table. if it does, iterate over each player to see if they have a
        # higher key. If any of them do, allow uploading of the log and
        # add/update players into the league table.

        try:
            ladder = Ladder.objects.get(
                internal_name=parser.map,
                internal_difficulty=parser.difficulty,
            )
        except Ladder.DoesNotExist:
            raise APIException("{parser.map} (parser.difficulty} is not a valid ladder")

        added = False
        for player in summary:
            if not player["is_player"]:
                continue

            queryset = LadderEntry.objects.filter(
                ladder__internal_name=parser.map,
                ladder__internal_difficulty=parser.difficulty,
                player=player["name"],
            )
            if queryset.count() == 0:
                LOGGER.info(
                    f"New Entry: {player['name']}: {parser.map} ({parser.difficulty}) - {player['dps']} DPS"
                )
                LadderEntry.objects.create(
                    player=player["name"],
                    data=player,
                    combatlog=self,
                    ladder=ladder,
                )
                added = True
            elif queryset.filter(data__dps__gt=player["dps"]):
                LOGGER.info(
                    f"Updated Entry: {player['name']}: {parser.map} ({parser.difficulty}) - {player['dps']} DPS"
                )
                queryset.update(
                    player=player["name"],
                    data=player,
                    combatlog=self,
                    ladder=ladder,
                )
                added = True

        if not added:
            raise APIException("No entries were updated")

        with transaction.atomic():
            if self.metadata is None:
                self.metadata = Metadata(
                    map=parser.map,
                    difficulty=parser.difficulty,
                    summary=summary,
                    dps_chart=parser.DPSChart,
                    damage_chart=parser.damageChart,
                    npc_dps_chart=parser.NPCDPSChart,
                    npc_damage_chart=parser.NPCDamageChart,
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
