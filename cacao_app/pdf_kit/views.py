# -*- coding: utf-8 -*-
import os
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404, HttpResponseRedirect

from wkhtmltopdf.views import PDFTemplateView

from cacao.models import Guide
from configuracion.models import Acerca


class PDFDownloadView(PDFTemplateView):
    template_name = 'pdf_kit/download.html'
    cmd_options = {
        'margin-top': 15,
        'margin-bottom': 15,
    }

    def set_filename(self, guide_name):
        self.filename = 'guia-%s.pdf' % guide_name
        return self.filename

    def get(self, request, *args, **kwargs):

        guide_number = self.request.GET.get('guide-id', None)
        pdf_path = os.path.join(settings.MEDIA_ROOT, 'guias/guia-%s.pdf' % guide_number)
        if os.path.exists(pdf_path):
            return HttpResponseRedirect('%sguias/guia-%s.pdf' % (settings.MEDIA_URL, guide_number))

        if not hasattr(settings, 'PDF_KIT_MODEL'):
            raise ImproperlyConfigured(
                'You need to set PDF_KIT_MODEL in settings')

        model = settings.PDF_KIT_MODEL.split('.')
        self.model = apps.get_model(app_label=model[0], model_name=model[1])
        return super(PDFDownloadView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PDFTemplateView, self).get_context_data(**kwargs)
        guide_number = self.request.GET.get('guide-id', None)

        if guide_number is None:
            raise Http404
        else:
            guide_obj = Guide.objects.get(number=guide_number)

        self.set_filename(guide_number)

        context['guide_obj'] = guide_obj

        context['content_obj'] = self.model.objects.filter(
            section__guide=guide_obj).order_by('section', 'peso')

        context['about_obj'] = Acerca.objects.get()

        return context
