"""Custom Template Tags for Ladder Entries"""

from django import template

from ladder.models import Ladder, LadderEntry

register = template.Library()


@register.filter
def rank(obj):
    """Return the ladder entry's rank"""
    key = f"data__{obj.ladder.metric}__gte"
    flt = {key: obj.data.get(obj.ladder.metric, 0)}
    return LadderEntry.objects.filter(ladder=obj.ladder).filter(**flt).count()


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
