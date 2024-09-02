"""LadderEntry Views"""

import logging

from core.filters import BaseFilterBackend
from core.pagination import PageNumberPagination
from django.core.exceptions import ImproperlyConfigured
from django.db.models.query import QuerySet
from django_filters.views import FilterView
from ladder.filters import LadderEntryFilter
from ladder.models import LadderEntry
from ladder.serializers import LadderEntrySerializer
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

LOGGER = logging.getLogger("django")


class LadderEntryViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
):
    """LadderEntry API"""

    queryset = LadderEntry.objects.filter(visible=True)
    serializer_class = LadderEntrySerializer
    pagination_class = PageNumberPagination
    filter_backends = (BaseFilterBackend, OrderingFilter)
    filterset_class = LadderEntryFilter
    ordering_fields = [
        "player",
        "ladder",
        "ladder__name",
        "ladder__difficulty",
    ]
    ordering = "-data__DPS"

    def __init__(self, *args, **kwargs):
        """Bootstrap our filter"""
        LadderEntryFilter()
        self.ordering_fields = LadderEntry.ordering_fields()


class LadderEntryView(FilterView):
    """LadderEntry View"""

    model = LadderEntry
    filter_backends = (BaseFilterBackend, OrderingFilter)
    filterset_class = LadderEntryFilter
    ordering = "-data__DPS"
    paginate_by = 15

    def get_queryset(self):
        """Custom Queryset - Hide unverified results"""
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {"cls": self.__class__.__name__}
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)

        return queryset.filter(visible=True)


class LadderInvitesView(FilterView):
    """LadderEntry View"""

    model = LadderEntry
    filter_backends = (BaseFilterBackend, OrderingFilter)
    filterset_class = LadderEntryFilter
    ordering = "-data__DPS"

    def get_queryset(self):
        return (
            LadderEntry.objects.filter(
                ladder__internal_name__in=[
                    "Infected Space",
                    "Hive Space",
                    "Bug Hunt",
                    "Nukara Prime: Transdimensional Tactics",
                ],
            )
            .exclude(ladder__difficulty="Any")
            .order_by("-data__DPS")
            .distinct("player", "ladder__difficulty")
        )
