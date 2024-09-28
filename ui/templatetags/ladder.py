"""Ladder Template Tags"""

import logging

from django import template
from django.utils import timezone

from ladder.models import Ladder, LadderEntry, Variant

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


@register.simple_tag
def get_current_variant():
    """Return the current Ladder"""
    return (
        Variant.objects.filter(start_date__lte=timezone.now())
        .order_by("-start_date")
        .first()
    )


@register.simple_tag
def get_variant_metrics(instance):
    """Return ladder metrics"""
    LOGGER.info(f"Ladder: {instance}")
    if instance:
        queryset = LadderEntry.objects.filter(ladder__variant=instance).order_by(
            "data__handle", "-data__DPS"
        )
    else:
        queryset = LadderEntry.objects.order_by("data__handle", "-data__DPS")

    return {
        "characters": {
            "count": queryset.values("player").distinct().count(),
            "space": {
                "1000000": queryset.filter(
                    ladder__is_space=True,
                    data__DPS__gte=1000000,
                )
                .values("player")
                .distinct()
                .count(),
                "500000": queryset.filter(
                    ladder__is_space=True,
                    data__DPS__gte=500000,
                )
                .values("player")
                .distinct()
                .count(),
                "300000": queryset.filter(
                    ladder__is_space=True,
                    data__DPS__gte=300000,
                )
                .values("player")
                .distinct()
                .count(),
                "100000": queryset.filter(
                    ladder__is_space=True,
                    data__DPS__gte=100000,
                )
                .values("player")
                .distinct()
                .count(),
            },
            "ground": {
                "10000": queryset.filter(
                    ladder__is_space=False,
                    data__DPS__gte=10000,
                )
                .values("player")
                .distinct()
                .count(),
                "5000": queryset.filter(
                    ladder__is_space=False,
                    data__DPS__gte=5000,
                )
                .values("player")
                .distinct()
                .count(),
                "3000": queryset.filter(
                    ladder__is_space=False,
                    data__DPS__gte=3000,
                )
                .values("player")
                .distinct()
                .count(),
                "1000": queryset.filter(
                    ladder__is_space=False,
                    data__DPS__gte=1000,
                )
                .values("player")
                .distinct()
                .count(),
            },
        },
        "accounts": {
            "count": queryset.values("data__handle").distinct().count(),
            "space": {
                "1000000": queryset.filter(
                    ladder__is_space=True,
                    data__DPS__gte=1000000,
                )
                .values("data__handle")
                .distinct()
                .count(),
                "500000": queryset.filter(
                    ladder__is_space=True,
                    data__DPS__gte=500000,
                )
                .values("data__handle")
                .distinct()
                .count(),
                "300000": queryset.filter(
                    ladder__is_space=True,
                    data__DPS__gte=300000,
                )
                .values("data__handle")
                .distinct()
                .count(),
                "100000": queryset.filter(
                    ladder__is_space=True,
                    data__DPS__gte=100000,
                )
                .values("data__handle")
                .distinct()
                .count(),
            },
            "ground": {
                "10000": queryset.filter(
                    ladder__is_space=False,
                    data__DPS__gte=10000,
                )
                .values("data__handle")
                .distinct()
                .count(),
                "5000": queryset.filter(
                    ladder__is_space=False,
                    data__DPS__gte=5000,
                )
                .values("data__handle")
                .distinct()
                .count(),
                "3000": queryset.filter(
                    ladder__is_space=False,
                    data__DPS__gte=3000,
                )
                .values("data__handle")
                .distinct()
                .count(),
                "1000": queryset.filter(
                    ladder__is_space=False,
                    data__DPS__gte=1000,
                )
                .values("data__handle")
                .distinct()
                .count(),
            },
        },
    }
