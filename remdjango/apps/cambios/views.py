# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.shortcuts import render, redirect
from apps.cambios.models import cambio

from apps.projecto.models import Projecto

from apps.cambios.forms import cambioForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# experimentar V

from django.views.generic import View
from reportlab.pdfgen import canvas

import os
from django.conf import settings
from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from xhtml2pdf import pisa 

class cambioCreate(CreateView):
	model = cambio
	form_class = cambioForm
	template_name = 'cambios/cambio_form.html'
	success_url = reverse_lazy('cambios:listar_cambio')

class cambioList(ListView):
	model = cambio
	template_name = 'cambios/cambio_list.html'
	paginate_by = 5

class cambioEdit(UpdateView):
	model = cambio
	form_class = cambioForm
	template_name = 'cambios/cambio_form.html'
	success_url = reverse_lazy('cambios:listar_cambio')

class cambioDelete(DeleteView):
	model = cambio
	template_name = 'cambios/cambio_delete.html'
	success_url = reverse_lazy('cambios:listar_cambio')
