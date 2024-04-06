""" Generate Ladder Variants """

import logging

from django.core.management.base import BaseCommand

from ladder.models import Variant

LOGGER = logging.getLogger("django")


class Command(BaseCommand):
    help = "Generate ladder variants"

    def handle(self, *args, **options):
        ladders = Variant.objects.get(name="Default").ladder_set.all()
        for ladder in ladders:
            ladder.create_variants()
