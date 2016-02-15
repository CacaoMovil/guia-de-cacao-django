# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Guide, Section, Content, Download


class GuideAdmin(admin.ModelAdmin):
    search_fields = ('number', 'name')
    list_display = ('name', 'number', 'tags_list')
    list_filter = ('tags',)
    fieldsets = [
        (None, {
            'fields': ['number', 'name', 'tags', 'description', 'image']}
         )
    ]

    def tags_list(self, obj):
        return ", ".join([t.name for t in obj.tags.all()])
    tags_list.short_description = 'Etiquetas'


class ContentInline(admin.StackedInline):
    model = Content
    exclude = ('slug',)
    extra = 1


class SectionAdmin(admin.ModelAdmin):
    model = Section
    inlines = [ContentInline, ]
    search_fields = ('title',)
    list_filter = ('title', 'guide')
    list_display = ('title', 'guide', 'peso')


class DownloadAdmin(admin.ModelAdmin):
    model = Download
    search_fields = ('guide',)
    list_filter = ('guide',)
    readonly_fields = ('checksum',)
    list_display = ('name', 'num_version', 'guide', 'date')
    fieldsets = [
        (None, {
            'fields': ['guide', 'num_version', 'file', 'checksum']}
         )
    ]

admin.site.register(Guide, GuideAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Download, DownloadAdmin)
