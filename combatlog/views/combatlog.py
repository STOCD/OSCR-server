""" CombatLog Views """

import logging

from django.db import transaction
from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from combatlog.models import CombatLog
from combatlog.serializers import (
    CombatLogSerializer,
    CombatLogUploadResponseSerializer,
    CombatLogUploadSerializer,
)
from core.pagination import PageNumberPagination

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

    @swagger_auto_schema(
        responses={200: CombatLogUploadResponseSerializer(many=True)},
    )
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

        data = serializer.validated_data["file"].read()

        with transaction.atomic():
            instance = CombatLog.objects.create()
            res = instance.update_metadata(data)
            serializer = CombatLogUploadResponseSerializer(data=res, many=True)
            serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            "200": openapi.Response(
                "File Attachment", schema=openapi.Schema(type=openapi.TYPE_FILE)
            )
        },
    )
    @action(
        detail=True,
        methods=["GET"],
        permission_classes=(),
    )
    def download(self, request, pk=None):
        """
        Combat Log Download

        Download the saved Combat Log
        """

        instance = self.get_object()
        data = instance.data()

        response = HttpResponse()
        response["Content-Disposition"] = f'attachment; filename="{instance}.log"'
        response["Content-Transfer-Encoding"] = "binary"
        response.write(data)
        return response
