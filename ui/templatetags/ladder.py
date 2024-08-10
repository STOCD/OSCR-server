"""Ladder Template Tags"""

import logging

from django import template

from ladder.models import Ladder

register = template.Library()
LOGGER = logging.getLogger("django")


@register.simple_tag
def get_ladders():
    """Return the list of ladders"""
    entries = {}
    for ladder in Ladder.objects.all():
        if entries.get(ladder.name) is None:
            entries[ladder.name] = {}
        if entries[ladder.name].get(ladder.difficulty) is None:
            entries[ladder.name][ladder.difficulty] = ladder.is_solo
    return entries
