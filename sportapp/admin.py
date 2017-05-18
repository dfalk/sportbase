#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Sport, Location, Worker, Tourney

class TourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end', 'participants', 'sport', 'location', 'time_text')
    list_editable = ('sport', 'date_start', 'date_end', 'participants', 'location', 'time_text',)

admin.site.register(Sport)
admin.site.register(Location)
admin.site.register(Worker)
admin.site.register(Tourney, TourneyAdmin)
