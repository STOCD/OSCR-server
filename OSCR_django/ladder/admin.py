""" CombatLog admin """

from django.contrib import admin

from .models import Ladder, LadderEntry

admin.site.register(Ladder)
admin.site.register(LadderEntry)
