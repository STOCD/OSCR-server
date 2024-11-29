"""CombatLog admin"""

from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from ladder.models import LadderEntry

from .models import CombatLog, Metadata


class LadderEntryInline(admin.StackedInline):
    model = LadderEntry
    extra = 1
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }


@admin.register(Metadata)
class MetadataAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }


@admin.register(CombatLog)
class CombatLogAdmin(admin.ModelAdmin):
    inlines = [LadderEntryInline]
    exclude = ["metadata"]
