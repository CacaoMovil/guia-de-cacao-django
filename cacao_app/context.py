# -*- coding: utf-8 -*-
from cacao.models import Guia

def guia_items(request):
	guia = Guia.objects.all().order_by('numero')
	dicc = {
			 'guia_items': guia,
		   }
	return dicc