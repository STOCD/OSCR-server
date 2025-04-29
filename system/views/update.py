"""Update Views"""

import logging

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from system.models import Update
from system.serializers import UpdateSerializer

LOGGER = logging.getLogger("django")


class UpdateViewSet(GenericViewSet):
    """Update API"""

    queryset = Update.objects.all()

    @action(
        detail=False,
        methods=["GET"],
        serializer_class=UpdateSerializer,
        permission_classes=(),
    )
    def latest(self, _):
        """Fetch information about the latest update"""
        return Response(self.get_serializer(Update.objects.latest("pk")).data)
