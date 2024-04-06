""" Variant Models """

from django.db import models

from core.models import BaseNameModel


class Variant(BaseNameModel):
    """Variant Model"""

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    is_ground_variant = models.BooleanField(default=True)
    is_space_variant = models.BooleanField(default=True)

    # Exclude subset-variants from the results. e.g.
    # The "default" variant can omit the Season 31 pre-Flagship Staffing nerf from its results.
    exclude_space = models.ManyToManyField(
        "ladder.Variant",
        blank=True,
        related_name="exclude_space_variant_set",
    )
    exclude_ground = models.ManyToManyField(
        "ladder.Variant",
        blank=True,
        related_name="exclude_ground_variant_set",
    )

    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date})"
