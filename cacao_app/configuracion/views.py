# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import TemplateView

from envelope.views import ContactView
from braces.views import FormMessagesMixin

from .models import Contacto, Acerca


class AboutView(TemplateView):
    """
    This method is used to render the
    Acerca model in the template
    """
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about'] = Acerca.objects.get()
        return context


class Contact(FormMessagesMixin, ContactView):
    """
    This class extend from django braces and ContactView
    is used to render all the Object from the Contacto model
    in the template.
    """
    form_invalid_message = _(u"There was en error in the contact form.")
    form_valid_message = _(u"Thank you for your message.")

    def get_context_data(self, **kwargs):
        context = super(Contact, self).get_context_data(**kwargs)
        context['contact'] = Contacto.objects.get()
        return context
