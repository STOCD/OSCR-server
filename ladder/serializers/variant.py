""" Variant Serializers """

from rest_framework import serializers

from ladder.models import Variant


class VariantSerializer(serializers.ModelSerializer):
    """Variant Serializer"""

    class Meta:
        model = Variant
        exclude = []
