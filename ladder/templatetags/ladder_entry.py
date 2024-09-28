"""Custom Template Tags for Ladder Entries"""

import logging

from django import template

from ladder.models import Ladder, LadderEntry

register = template.Library()

LOGGER = logging.getLogger("django")


@register.simple_tag
def rank(obj, request):
    """Return the ladder entry's rank"""
    key = f"data__{obj.ladder.metric}__gt"
    flt = {key: obj.data.get(obj.ladder.metric, 0)}
    query = {}
    for k, v in request.GET.items():
        if k not in ["ordering", "page", "page_size"] and v:
            query[k] = v
    return (
        LadderEntry.objects.filter(**query).filter(visible=True).filter(**flt).count()
        + 1
    )


@register.simple_tag
def ladder_rank(obj, request):
    """Return the ladder entry's rank"""
    key = f"data__{obj.ladder.metric}__gt"
    flt = {key: obj.data.get(obj.ladder.metric, 0)}
    return (
        LadderEntry.objects.filter(ladder=obj.ladder)
        .filter(visible=True)
        .filter(**flt)
        .count()
        + 1
    )


@register.simple_tag
def ladder_variants():
    """Return the list of ladder variants"""
    return Ladder.objects.values_list("variant", flat=True).distinct()


@register.simple_tag
def ladder_names():
    """Return the list of ladder variants"""
    return Ladder.objects.values_list("name", flat=True).distinct()


@register.simple_tag
def ladder_difficulties():
    """Return the list of ladder variants"""
    return (
        Ladder.objects.exclude(difficulty=None)
        .values_list("difficulty", flat=True)
        .distinct()
    )


@register.simple_tag
def ladder_entry_channels(instance):
    # <pre></pre>
    # /channel_invite "{{channel}}" {{entry.player}} # {{entry.data.DPS|floatformat:0}} DPS
    channels = []
    if instance.ladder.internal_name in [
        "Infected Space",
    ] and instance.ladder.internal_difficulty in ["Advanced", "Elite"]:
        if instance.data.get("DPS", 0) >= 500000:
            channels.append("DPS-#s-Prime")
        if instance.data.get("DPS", 0) >= 150000:
            channels.append("DPS-#s-Elites")
    elif instance.ladder.internal_name in [
        "Hive Space",
    ] and instance.ladder.internal_difficulty in ["Elite"]:
        if instance.data.get("DPS", 0) >= 500000:
            channels.append("DPS-#s-Prime")
        if instance.data.get("DPS", 0) >= 150000:
            channels.append("DPS-#s-Elites")
    elif instance.ladder.internal_name in [
        "Bug Hunt",
        "Nukera Prime: Transdimensional Tactics",
    ]:
        if instance.data.get("DPS", 0) >= 1000:
            channels.append("DPS-#s-Ground")
    return channels
