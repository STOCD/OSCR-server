""" LadderEntry Views """

import logging

from django_filters.views import FilterView
from rest_framework.filters import OrderingFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from core.filters import BaseFilterBackend
from core.pagination import PageNumberPagination
from ladder.filters import LadderEntryFilter
from ladder.models import LadderEntry
from ladder.serializers import LadderEntrySerializer

LOGGER = logging.getLogger("django")


class LadderEntryViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
):
    """LadderEntry API"""

    queryset = LadderEntry.objects.all()
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
