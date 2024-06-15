""" LadderEntry Serializers """

import logging

from rest_framework import serializers

from ladder.models import LadderEntry

LOGGER = logging.getLogger("django")


class LadderEntrySerializer(serializers.ModelSerializer):
    """LadderEntry Serializer"""

    date = serializers.SerializerMethodField(read_only=True)
    rank = serializers.SerializerMethodField(read_only=True)

    def get_date(self, obj):
        """Return the date of the combat log"""
        return obj.combatlog.metadata.date_time

    def get_rank(self, obj) -> int:
        """Return the rank of the ladder entry with respect to the ladder"""
        key = f"data__{obj.ladder.metric}__gt"
        flt = {key: obj.data.get(obj.ladder.metric, 0)}
        query = {}
        for k, v in self.context["request"].GET.items():
            if k not in ["ordering", "page", "page_size"] and v:
                query[k] = v
        return (
            LadderEntry.objects.filter(**query)
            .filter(visible=True)
            .filter(**flt)
            .count()
            + 1
        )

    class Meta:
        model = LadderEntry
        exclude = ["visible"]
