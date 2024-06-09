""" LadderEntry Filter """

import decimal
import logging

import django_filters.rest_framework as filters
from django.db.models import JSONField

from core.filters import BaseFilterSet
from ladder.models import LadderEntry

LOGGER = logging.getLogger("django")

CHAR_FILTERS = [
    "exact",
    "iexact",
    "contains",
    "icontains",
    "istartswith",
    "startswith",
    "endswith",
    "iendswith",
    "iregex",
    "regex",
]


class LadderEntryFilter(BaseFilterSet):
    """Filter for model"""

    class Meta:
        """Meta class for filter"""

        model = LadderEntry
        fields = {
            "player": CHAR_FILTERS,
            "ladder": ["exact"],
            "ladder__name": CHAR_FILTERS,
            "ladder__difficulty": CHAR_FILTERS,
            "ladder__variant__name": CHAR_FILTERS,
            "ladder__is_solo": ["exact"],
        }
        filter_overrides = {
            JSONField: {
                "filter_class": filters.CharFilter,
            },
        }

    def filter_json_field_value(self, queryset, name, value):
        if type(value) in [decimal.Decimal]:
            value = float(value)
        return queryset.filter(**{name: value})

    def __init__(self, *args, **kwargs):
        """Custom init to populate filters"""
        super().__init__(*args, **kwargs)

        if self.queryset.exists():
            for k, v in self.queryset.first().data.items():
                if type(v) in [float, int]:
                    for expr in ["lt", "gt", "lte", "gte"]:
                        self.base_filters[f"data__{k}__{expr}"] = filters.NumberFilter(
                            field_name=f"data__{k}__{expr}",
                            label=f"data__{k}__{expr}",
                            method="filter_json_field_value",
                        )
                    self.base_filters[f"data__{k}"] = filters.NumberFilter(
                        field_name=f"data__{k}",
                        label=f"data__{k}",
                        method="filter_json_field_value",
                    )
                elif type(v) in [bool]:
                    self.base_filters[f"data__{k}"] = filters.BooleanFilter(
                        field_name=f"data__{k}",
                        label=f"data__{k}",
                        method="filter_json_field_value",
                    )
                else:
                    for expr in CHAR_FILTERS:
                        self.base_filters[f"data__{k}__{expr}"] = filters.CharFilter(
                            field_name=f"data__{k}__{expr}",
                            label=f"data__{k}__{expr}",
                            method="filter_json_field_value",
                        )
                    self.base_filters[f"data__{k}"] = filters.CharFilter(
                        field_name=f"data__{k}",
                        label=f"data__{k}",
                        method="filter_json_field_value",
                    )
