""" Metadata Models """

from django.db import models

from core.models import BaseModel


class Metadata(BaseModel):
    """Combat Log Model"""

    map = models.TextField()
    difficulty = models.TextField(null=True, default=None)
    summary = models.JSONField()
    date_time = models.DateTimeField(null=True, default=None)

    damage_out = models.JSONField(null=True, default=None)
    damage_in = models.JSONField(null=True, default=None)
    heal_out = models.JSONField(null=True, default=None)
    heal_in = models.JSONField(null=True, default=None)

    def __str__(self):
        return f"{self.date_time} {self.map} ({self.difficulty})"
