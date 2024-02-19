""" LadderEntry Serializers """

from ladder.models import LadderEntry
from rest_framework import serializers


class LadderEntrySerializer(serializers.ModelSerializer):
    """LadderEntry Serializer"""

    date = serializers.SerializerMethodField(read_only=True)

    def get_date(self, obj):
        """Return the date of the combat log"""
        return obj.combatlog.metadata.date_time

    class Meta:
        model = LadderEntry
        fields = "__all__"
