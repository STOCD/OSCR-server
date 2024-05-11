""" CombatLog admin """

from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from .models import Ladder, LadderEntry, Variant

admin.site.register(Ladder)
admin.site.register(Variant)


@admin.register(LadderEntry)
class LadderEntryAdmin(admin.ModelAdmin):
    list_display = [
        "player",
        "ladder__name",
        "ladder__difficulty",
        "ladder__variant__name",
        "dps",
        "damage",
        "combat_time",
        "build",
    ]
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }

    @admin.display(ordering="ladder__name")
    def ladder__name(self, obj):
        return obj.ladder.name

    @admin.display(ordering="ladder__difficulty")
    def ladder__difficulty(self, obj):
        return obj.ladder.difficulty

    @admin.display(ordering="ladder__variant__name")
    def ladder__variant__name(self, obj):
        return obj.ladder.variant.name

    @admin.display(ordering="data__DPS")
    def dps(self, obj):
        return int(obj.data.get("DPS"))

    @admin.display(ordering="data__total_damage")
    def damage(self, obj):
        return int(obj.data.get("total_damage"))

    @admin.display(ordering="data__combat_time")
    def combat_time(self, obj):
        return int(obj.data.get("combat_time"))

    @admin.display(ordering="data__build")
    def build(self, obj):
        return obj.data.get("build")
