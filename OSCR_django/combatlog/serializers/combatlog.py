""" CombatLog Serializers """

from combatlog.models import CombatLog
from rest_framework import serializers

from .metadata import MetadataSerializer


class CombatLogSerializer(serializers.ModelSerializer):
    """CombatLog Serializer"""

    metadata = MetadataSerializer()

    class Meta:
        model = CombatLog
        exclude = [
            "file",
        ]


class CombatLogUploadSerializer(serializers.Serializer):
    """CombatLog Upload Serializer"""

    file = serializers.FileField()
