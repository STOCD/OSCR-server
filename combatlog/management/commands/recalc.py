import logging

from combatlog.models import CombatLog
from django.core.management.base import BaseCommand

LOGGER = logging.getLogger("django")


class Command(BaseCommand):
    help = "Recalculates Combat Log Metadata"

    def handle(self, *args, **options):
        for combatlog in CombatLog.objects.all():
            try:
                combatlog.update_metadata_from_remote()
            except Exception as e:
                LOGGER.info(f"{e}: {combatlog}")
