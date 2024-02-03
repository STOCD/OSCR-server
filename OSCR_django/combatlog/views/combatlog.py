""" CombatLog Views """

import logging

from combatlog.models import CombatLog
from combatlog.serializers import CombatLogSerializer, CombatLogUploadSerializer
from core.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

LOGGER = logging.getLogger("django")


class CombatLogViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
):
    """Combat Log API"""

    queryset = CombatLog.objects.all()
    serializer_class = CombatLogSerializer
    pagination_class = PageNumberPagination

    @action(
        detail=False,
        methods=["POST"],
        serializer_class=CombatLogUploadSerializer,
        parser_classes=(MultiPartParser,),
        permission_classes=(),
    )
    def upload(self, request):
        """
        Combat Log Upload

        Uploads a Combat Log for analysis.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        CombatLog.objects.create(file=serializer.validated_data["file"])

        return Response(status=200)
