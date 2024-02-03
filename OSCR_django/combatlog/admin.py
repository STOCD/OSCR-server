""" CombatLog admin """

from django.contrib import admin

from .models import CombatLog, Metadata

admin.site.register(CombatLog)
admin.site.register(Metadata)
