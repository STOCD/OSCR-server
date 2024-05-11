""" Bulk import combat logs from a directory """

import gzip
import logging
import os
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import transaction

from combatlog.models import CombatLog

LOGGER = logging.getLogger("django")


def is_gz_file(filepath):
    with open(filepath, "rb") as test_f:
        return test_f.read(2) == b"\x1f\x8b"


class Command(BaseCommand):
    help = "Bulk import combat logs from a directory"

    def add_arguments(self, parser):
        parser.add_argument("dir", type=str)

    def handle(self, *args, **options):
        if not os.path.exists(options["dir"]):
            raise Exception(f"Directory does not exist: {options['dir']}")

        for entry in Path(options["dir"]).glob("*"):
            if entry.is_file():
                try:
                    with transaction.atomic():
                        instance = CombatLog.objects.create()
                        with open(entry, "rb") as file:
                            if is_gz_file(entry):
                                data = file.read()
                            else:
                                data = gzip.compress(file.read())
                            instance.update_metadata(data)
                except Exception as e:
                    LOGGER.info(f"Failed to import {entry}: {e}")
