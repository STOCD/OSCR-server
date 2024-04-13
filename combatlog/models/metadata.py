""" Metadata Models """

from core.models import BaseModel
from django.db import models


class Metadata(BaseModel):
    """Combat Log Model"""

    map = models.TextField()
    difficulty = models.TextField(null=True, default=None)
    summary = models.JSONField()
    date_time = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return f"{self.date_time} {self.map} ({self.difficulty})"
