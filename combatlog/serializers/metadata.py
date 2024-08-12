"""Metadata Serializers"""

from rest_framework import serializers

from combatlog.models import Metadata


class MetadataSerializer(serializers.ModelSerializer):
    """Metadata Serializer"""

    class Meta:
        model = Metadata
        exclude = [
            "damage_out",
            "damage_in",
            "heal_out",
            "heal_in",
        ]
