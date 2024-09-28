""" LadderEntry Models """

from django.db import models

from core.models import BaseModel

from .ladder import Ladder


class LadderEntry(BaseModel):
    """LadderEntry Model"""

    player = models.TextField()
    data = models.JSONField()

    combatlog = models.ForeignKey(
        "combatlog.CombatLog", on_delete=models.CASCADE)
    ladder = models.ForeignKey(Ladder, on_delete=models.CASCADE)

    visible = models.BooleanField(default=True)

    def ladder_entry_channels(self):
        channels = []
        if self.ladder.internal_name in [
            "Infected Space",
        ] and self.ladder.internal_difficulty in ["Advanced", "Elite"]:
            if self.data.get("DPS", 0) >= 500000:
                channels.append("DPS-#s-Prime")
            if self.data.get("DPS", 0) >= 150000:
                channels.append("DPS-#s-Elites")
        elif self.ladder.internal_name in [
            "Hive Space",
        ] and self.ladder.internal_difficulty in ["Elite"]:
            if self.data.get("DPS", 0) >= 500000:
                channels.append("DPS-#s-Prime")
            if self.data.get("DPS", 0) >= 150000:
                channels.append("DPS-#s-Elites")
        elif self.ladder.internal_name in [
            "Bug Hunt",
            "Nukera Prime: Transdimensional Tactics",
        ]:
            if self.data.get("DPS", 0) >= 1000:
                channels.append("DPS-#s-Ground")
        return channels

    def __str__(self):
        return f"{self.player} | {self.ladder.name} ({self.ladder.difficulty}, {self.ladder.variant.name}) - {self.data['DPS']:,.0f} DPS"

    @classmethod
    def ordering_fields(cls):
        base_fields = ["player", "ladder__name", "ladder__difficulty"]
        data_fields = []
        """Custom Method to get Ordering Fields"""
        if LadderEntry.objects.count():
            for k, _ in LadderEntry.objects.first().data.items():
                data_fields.append(f"data__{k}")

        return base_fields + data_fields
