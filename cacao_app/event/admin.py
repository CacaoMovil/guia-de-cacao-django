# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Event, CountryEvent


class CountryEvent(admin.StackedInline):
    model = CountryEvent
    extra = 1


class EventAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('start', 'end')
    list_display = ('name', 'start', 'end')
    inlines = [CountryEvent, ]

admin.site.register(Event, EventAdmin)
