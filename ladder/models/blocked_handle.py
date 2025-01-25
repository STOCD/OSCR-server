"""BlockedHandle Models"""

from django.db import models


class BlockedHandle(models.Model):
    """BlockedHandle Model"""

    handle = models.TextField(help_text="Player's @handle. You need to include the '@'")

    def __str__(self):
        return f"{self.handle}"
