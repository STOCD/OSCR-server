""" Base Filter """

from django_filters.rest_framework import DjangoFilterBackend, FilterSet


class BaseFilterSet(FilterSet):
    """Base FilterSet"""


class BaseFilterBackend(DjangoFilterBackend):
    """Base Filter Backend"""

    def filter_json_field_value(self, queryset, name, value):
        return queryset.filter(**{name: value})
