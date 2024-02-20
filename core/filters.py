""" Base Filter """

import logging

import django_filters.rest_framework as filters

LOGGER = logging.getLogger("django")


class BaseFilterSet(filters.FilterSet):
    """Base FilterSet"""


class BaseFilterBackend(filters.DjangoFilterBackend):
    """Base Filter Backend"""
