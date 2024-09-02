"""CombatLog Serializers"""

from rest_framework import serializers

from combatlog.models import CombatLog

from .metadata import MetadataSerializer


class CombatLogSerializer(serializers.ModelSerializer):
    """CombatLog Serializer"""

    metadata = MetadataSerializer()

    class Meta:
        model = CombatLog
        exclude = ["name"]


class CombatLogUploadSerializer(serializers.Serializer):
    """CombatLog Upload Serializer"""

    file = serializers.FileField()


class CombatLogUploadV2Serializer(serializers.Serializer):
    """CombatLog Upload Serializer"""

    file = serializers.FileField()


class CombatLogUploadResponseSerializer(serializers.Serializer):
    """CombatLog Upload Response Serializer"""

    name = serializers.CharField()
    updated = serializers.BooleanField()
    detail = serializers.CharField()
    value = serializers.FloatField()


class CombatLogUploadV2ResponseSerializer(serializers.Serializer):
    """CombatLog Upload Response Serializer"""

    results = CombatLogUploadResponseSerializer(
        many=True,
        required=False,
        allow_null=True,
    )
    combatlog = serializers.IntegerField(required=False, allow_null=True)
    detail = serializers.CharField()
