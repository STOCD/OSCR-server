""" LadderEntry Filter """

from core.filters import BaseFilterSet
from django.db.models import JSONField
from django_filters.rest_framework import CharFilter
from ladder.models import LadderEntry


class LadderEntryFilter(BaseFilterSet):
    """Filter for Tasks API"""

    class Meta:
        """Meta class for the application filter"""

        model = LadderEntry
        fields = "__all__"
        filter_overrides = {
            JSONField: {
                "filter_class": CharFilter,
            },
        }
