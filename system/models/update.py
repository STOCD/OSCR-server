"""Update Model"""

from django.db import models

from core.models import BaseModel


class Update(BaseModel):
    """Our Implementation of the Abstract Update"""

    version = models.TextField()
    url_appimage = models.TextField(blank=True)
    url_msi = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.version
