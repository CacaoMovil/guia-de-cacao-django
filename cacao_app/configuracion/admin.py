# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from solo.admin import SingletonModelAdmin
from suit_ckeditor.widgets import CKEditorWidget

from .models import Contacto, Acerca

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto

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
            'informacion_contacto': CKEditorWidget(editor_options=_ck_editor_config),
            'contacto_general': CKEditorWidget(editor_options=_ck_editor_config),
        }
    

class ContactoAdmin(SingletonModelAdmin):
    form = ContactoForm
    fieldsets = [
      (None, {
        'fields': ['informacion_contacto', 'contacto_general']}
      )
    ]

class AcercaForm(ModelForm):
    class Meta:
        model = Acerca

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
            'informacion_bienvenida': CKEditorWidget(editor_options=_ck_editor_config),
        }
    

class AcercaAdmin(SingletonModelAdmin):
    form = AcercaForm
    fieldsets = [
      (None, {
        'fields': ['informacion_bienvenida']}
      )
    ]

admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Acerca, AcercaAdmin)