""" Ladder Serializers """

from rest_framework import serializers

from ladder.models import Ladder


class LadderSerializer(serializers.ModelSerializer):
    """Ladder Serializer"""

    variant_name = serializers.SerializerMethodField(read_only=True)

    def get_variant_name(self, instance):
        """Returns the variant name"""
        return instance.variant.name

    class Meta:
        model = Ladder
        exclude = [
            "internal_name",
            "internal_difficulty",
            "manual_review_threshold",
        ]
