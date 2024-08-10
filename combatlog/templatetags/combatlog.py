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
    res.append(instance.metadata.difficulty)
    for _, player in instance.metadata.summary:
        res.append(f"{player['handle']} - {int(player['DPS'])}")
    return " | ".join(res)
