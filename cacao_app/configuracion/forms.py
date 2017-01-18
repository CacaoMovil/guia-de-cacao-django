# -*- coding: utf-8 -*-

from collections import OrderedDict

from django import forms
from django.utils.translation import ugettext_lazy as _

from envelope.forms import ContactForm


class ContactForm(ContactForm):
    template_name = "envelope/contact_email.txt"
    html_template_name = "envelope/contact_email.html"

    phone = forms.CharField(label='Teléfono', required=False)
    country = forms.CharField(label='País', required=False)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False

ContactForm.base_fields = OrderedDict(
    (k, ContactForm.base_fields[k])
    for k in [
        'sender', 'subject', 'email', 'phone', 'country',  'message',
    ]
)
