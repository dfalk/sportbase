#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Sport, Location, Worker, Tourney

class TourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end', 'participants')
    list_editable = ('date_start', 'date_end', 'participants')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('title', 'typer')
    list_editable = ('typer',)

admin.site.register(Sport)
admin.site.register(Location, LocationAdmin)
admin.site.register(Worker)
admin.site.register(Tourney, TourneyAdmin)
