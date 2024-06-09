""" Ladder Views """

import logging

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from core.filters import BaseFilterBackend
from core.pagination import AllResultsPagination
from ladder.filters import LadderFilter
from ladder.models import Ladder
from ladder.serializers import LadderSerializer

LOGGER = logging.getLogger("django")


class LadderViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
):
    """Ladder API"""

    queryset = Ladder.objects.all()
    serializer_class = LadderSerializer
    pagination_class = AllResultsPagination
    filter_backends = (BaseFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = LadderFilter
    ordering_fields = "__all__"
    ordering = ["variant__name", "id"]
