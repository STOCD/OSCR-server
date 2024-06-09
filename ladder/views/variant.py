""" Variant Views """

import logging

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from core.filters import BaseFilterBackend
from core.pagination import AllResultsPagination
from ladder.filters import VariantFilter
from ladder.models import Variant
from ladder.serializers import VariantSerializer

LOGGER = logging.getLogger("django")


class VariantViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
):
    """Variant API"""

    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    pagination_class = AllResultsPagination
    filter_backends = (BaseFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = VariantFilter
    ordering_fields = "__all__"
    ordering = ["name"]
