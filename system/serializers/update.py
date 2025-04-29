"""Update Serializers"""

from rest_framework import serializers

from system.models import Update


class UpdateSerializer(serializers.ModelSerializer):
    """Update Serializer"""

    class Meta:
        model = Update
        fields = "__all__"
