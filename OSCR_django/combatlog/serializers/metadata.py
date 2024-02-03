""" Metadata Serializers """

from combatlog.models import Metadata
from rest_framework import serializers


class MetadataSerializer(serializers.ModelSerializer):
    """Metadata Serializer"""

    class Meta:
        model = Metadata
        exclude = [
            "dps_chart",
            "damage_chart",
            "npc_dps_chart",
            "npc_damage_chart",
        ]
