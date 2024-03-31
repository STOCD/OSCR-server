""" CombatLog admin """

from django.contrib import admin

from .models import Ladder, LadderEntry, Variant

admin.site.register(Ladder)
admin.site.register(LadderEntry)
admin.site.register(Variant)
