""" LadderEntry Serializers """

from ladder.models import LadderEntry
from rest_framework import serializers


class LadderEntrySerializer(serializers.ModelSerializer):
    """LadderEntry Serializer"""

    date = serializers.SerializerMethodField(read_only=True)
    rank = serializers.SerializerMethodField(read_only=True)

    def get_date(self, obj):
        """Return the date of the combat log"""
        return obj.combatlog.metadata.date_time

    def get_rank(self, obj) -> int:
        """Return the rank of the ladder entry with respect to the ladder"""
        key = f"data__{obj.ladder.metric}__gte"
        flt = {key: obj.data.get(obj.ladder.metric, 0)}
        return LadderEntry.objects.filter(ladder=obj.ladder).filter(**flt).count()

    class Meta:
        model = LadderEntry
        fields = "__all__"
