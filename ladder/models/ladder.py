""" Ladder Models """

from core.models import BaseModel
from django.db import models

from .variant import Variant


class Ladder(BaseModel):
    """Ladder Model"""

    name = models.TextField()
    difficulty = models.TextField()
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, null=True)
    is_solo = models.BooleanField(default=False)
    is_space = models.BooleanField(default=True)
    metric = models.TextField()

    internal_name = models.TextField()
    internal_difficulty = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.difficulty}) - {self.metric}{' (Solo)' if self.is_solo else ''}"
