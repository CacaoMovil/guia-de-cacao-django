# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from envelope.views import ContactView
from braces.views import FormMessagesMixin

from .models import Contacto, Acerca

def acerca(request, template="about.html"):
    """
    This method is used to render the
    Acerca model in the template
    """
    try:
        about = Acerca.objects.get()
    except Acerca.DoesNotExist:
        raise Http404
    return render(request, template, {'about': about})

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
