""" Ladder Models """

import logging

from django.db import models

from core.models import BaseModel

from .variant import Variant

LOGGER = logging.getLogger("django")


class Ladder(BaseModel):
    """Ladder Model"""

    name = models.TextField()
    difficulty = models.TextField()
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    is_solo = models.BooleanField(default=False)
    is_space = models.BooleanField(default=True)
    metric = models.TextField()

    internal_name = models.TextField()
    internal_difficulty = models.TextField()

    def create_variant(self, variant):
        """Create variant of ladder"""
        if not Ladder.objects.filter(
            name=self.name,
            difficulty=self.difficulty,
            variant=variant,
            is_solo=self.is_solo,
            is_space=self.is_space,
            metric=self.metric,
            internal_name=self.internal_name,
            internal_difficulty=self.internal_difficulty,
        ).count():
            LOGGER.info(f"Creating variant {variant.name} for ladder {self.name}")
            self.pk = None
            self.variant = variant
            self.save()

    def create_variants(self):
        """Create missing variants of ladder"""
        for variant in Variant.objects.exclude(pk=self.variant.pk):
            if self.is_space and variant.is_space_variant:
                self.create_variant(variant)
            elif not self.is_space and variant.is_ground_variant:
                self.create_variant(variant)

    def __str__(self):
        return f"{' [Solo]' if self.is_solo else ''} ({self.variant.name}) {self.name} {self.difficulty} {self.metric}"
