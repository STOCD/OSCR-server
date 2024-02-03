""" LadderEntry Serializers """

from ladder.models import LadderEntry
from rest_framework import serializers


class LadderEntrySerializer(serializers.ModelSerializer):
    """LadderEntry Serializer"""

    class Meta:
        model = LadderEntry
        fields = "__all__"
