# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.shortcuts import render, redirect
from apps.conflictos.models import conflicto, defecto

from apps.projecto.models import Projecto

from apps.conflictos.forms import conflictoForm, defectoForm

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

class conCreate(CreateView):
	model = conflicto
	form_class = conflictoForm
	template_name = 'conflictos/con_form.html'
	success_url = reverse_lazy('conflictos:listar_con')

class conList(ListView):
	model = conflicto
	template_name = 'conflictos/con_list.html'
	paginate_by = 5

class conEdit(UpdateView):
	model = conflicto
	form_class = conflictoForm
	template_name = 'conflictos/con_form.html'
	success_url = reverse_lazy('conflictos:listar_con')

class conDelete(DeleteView):
	model = conflicto
	template_name = 'conflictos/con_delete.html'
	success_url = reverse_lazy('conflictos:listar_con')

# defecto

class defCreate(CreateView):
	model = defecto
	form_class = defectoForm
	template_name = 'conflictos/def_form.html'
	success_url = reverse_lazy('conflictos:listar_def')

class defList(ListView):
	model = defecto
	template_name = 'conflictos/def_list.html'
	paginate_by = 5

class defEdit(UpdateView):
	model = defecto
	form_class = defectoForm
	template_name = 'conflictos/def_form.html'
	success_url = reverse_lazy('conflictos:listar_def')

class defDelete(DeleteView):
	model = defecto
	template_name = 'conflictos/def_delete.html'
	success_url = reverse_lazy('conflictos:listar_def')