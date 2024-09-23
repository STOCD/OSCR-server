""" Generate Ladder Variants """

import logging

from django.core.management.base import BaseCommand

from ladder.models import LadderEntry

LOGGER = logging.getLogger("django")


class Command(BaseCommand):
    help = "Display Ladder Metrics"

    def handle(self, *args, **options):
        max_bucket = 5000000
        idx = 0
        while idx <= max_bucket:
            entries = LadderEntry.objects.order_by(
                "data__handle", "-data__DPS").distinct("data__handle").filter(data__DPS__gte=idx)
            print(f"{idx},{len(entries)}")
            idx += 10000
