"""Custom Template Tags for Combatlog"""

import logging

from django import template

register = template.Library()

LOGGER = logging.getLogger("django")


@register.simple_tag
def summary(instance):
    """Return a summary of the combat log"""
    res = []
    res.append(instance.metadata.map)
    res.append(f"{instance.metadata.difficulty} Difficulty")
    res.append("DPS")
    players = []
    for _, player in instance.metadata.summary:
        print(player)
        players.append(
            {
                "name": player["handle"],
                "DPS": int(player["DPS"]),
            }
        )

    players = sorted(players, reverse=True, key=lambda player: player["DPS"])
    for player in players:
        res.append(f"{player['name']} - {int(player['DPS']):,}")

    return " | ".join(res)
