""" Metadata Models """

from core.models import BaseModel
from django.db import models


class Metadata(BaseModel):
    """Combat Log Model"""

    map = models.TextField(default="Unknown")
    difficulty = models.TextField(default="Unknown")
    summary = models.JSONField(null=True, default=None)

    dps_chart = models.JSONField(null=True, default=None)
    damage_chart = models.JSONField(null=True, default=None)

    npc_dps_chart = models.JSONField(null=True, default=None)
    npc_damage_chart = models.JSONField(null=True, default=None)

    def __str__(self):
        return f"{self.map} ({self.difficulty})"
