""" Ladder Serializers """

from ladder.models import Ladder
from rest_framework import serializers


class LadderSerializer(serializers.ModelSerializer):
    """Ladder Serializer"""

    class Meta:
        model = Ladder
        exclude = [
            "internal_name",
            "internal_difficulty",
        ]
