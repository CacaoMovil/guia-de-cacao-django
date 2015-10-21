# -*- coding: utf-8 -*-
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from wkhtmltopdf.views import PDFTemplateView

from cacao.models import Guide, Content
from configuracion.models import Acerca


class PDFDownloadView(PDFTemplateView):
    filename = ''
    template_name = 'pdf_kit/download.html'
    cmd_options = {
        'margin-top': 15,
        'margin-bottom': 15,
    }
    # allowed_methods = ['post']

    def get(self, request, *args, **kwargs):
        if not hasattr(settings, 'PDF_KIT_MODEL'):
            raise ImproperlyConfigured(
                'You need to set PDF_KIT_MODEL in settings')

        model = settings.PDF_KIT_MODEL.split('.')
        self.model = apps.get_model(app_label=model[0], model_name=model[1])
        return super(PDFDownloadView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PDFTemplateView, self).get_context_data(**kwargs)
        guide_number = self.request.GET.get('guide-id', None)
        self.filename = 'guia-%s.pdf' % guide_number
        guide_obj = Guide.objects.get(number=guide_number)
        content_obj = Content.objects.filter(
            section__guide=guide_obj).order_by('section', 'peso')
        about_obj = Acerca.objects.get()

        context = {
            'guide_obj': guide_obj,
            'content_obj': content_obj,
            'about_obj': about_obj,
        }
        return context
