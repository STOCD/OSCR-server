""" Ladder Models """

from core.models import BaseModel
from django.db import models


class Ladder(BaseModel):
    """Ladder Model"""

    name = models.TextField()
    difficulty = models.TextField()
    metric = models.TextField()
    is_solo = models.BooleanField(default=False)

    internal_name = models.TextField()
    internal_difficulty = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.difficulty}) - {self.metric}{' (Solo)' if self.is_solo else ''}"
