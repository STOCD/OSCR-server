"""Metadata Models"""

from django.db import models

from core.models import BaseModel


class Ability(BaseModel):
    """Combat Log Model"""

    name = models.TextField()
    prohibited = models.BooleanField()

    def __str__(self):
        return self.name + " (prohibited)" if self.prohibited else ""
