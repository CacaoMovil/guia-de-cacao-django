# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from suit_ckeditor.widgets import CKEditorWidget

from .models import Guia, Seccion, Contenido, Descarga


class GuiaForm(ModelForm):
    class Meta:
        model = Guia

        _ck_editor_toolbar = [
            {'name': 'basicstyles', 'groups': ['basicstyles', 'cleanup']},
            {'name': 'paragraph',
             'groups': ['list', 'indent', 'blocks', 'align']},
            {'name': 'document', 'groups': ['mode']}, '/',
            {'name': 'styles'}, {'name': 'colors'},
            {'name': 'insert_custom',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule']},
            {'name': 'about'}]

        _ck_editor_config = {'autoGrow_onStartup': True,
                             'autoGrow_minHeight': 100,
                             'autoGrow_maxHeight': 250,
                             'extraPlugins': 'autogrow',
                             'toolbarGroups': _ck_editor_toolbar}

        widgets = {
            'descripcion': CKEditorWidget(editor_options=_ck_editor_config),
        }
    

class GuiaAdmin(ModelAdmin):
    form = GuiaForm
    search_fields = ('numero', 'nombre')
    list_display = ('nombre', 'numero')
    fieldsets = [
      (None, {
        'fields': ['numero', 'nombre', 'descripcion', 'imagen_portada']}
      )
    ]
    

class SeccionAdmin(admin.ModelAdmin):
    model = Seccion
    search_fields = ('titulo',)
    list_filter = ('titulo', 'guia')
    list_display = ('titulo','guia')

class ContenidoForm(ModelForm):
    class Meta:
        model = Contenido

        _ck_editor_toolbar = [
            {'name': 'basicstyles', 'groups': ['basicstyles', 'cleanup']},
            {'name': 'paragraph',
             'groups': ['list', 'indent', 'blocks', 'align']},
            {'name': 'document', 'groups': ['mode']}, '/',
            {'name': 'styles'}, {'name': 'colors'},
            {'name': 'insert_custom',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule']},
            {'name': 'about'}]

        _ck_editor_config = {'autoGrow_onStartup': True,
                             'autoGrow_minHeight': 100,
                             'autoGrow_maxHeight': 250,
                             'extraPlugins': 'autogrow',
                             'toolbarGroups': _ck_editor_toolbar}

        widgets = {
            'contenido': CKEditorWidget(editor_options=_ck_editor_config),
        }

class ContenidoAdmin(ModelAdmin):
    form = ContenidoForm
    search_fields = ('titulo',)
    list_filter = ('seccion',)
    list_display = ('titulo','seccion')
    fieldsets = [
      (None, {
        'fields': ['seccion', 'titulo', 'contenido', 'peso', 'imagen_contenido']}
      )
    ]


admin.site.register(Guia, GuiaAdmin)
admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Contenido, ContenidoAdmin)
admin.site.register(Descarga)