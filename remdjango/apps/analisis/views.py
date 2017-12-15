# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.shortcuts import render, redirect
from apps.analisis.models import diagrama_secuencia, asociacion, roles

from apps.projecto.models import Projecto

from apps.analisis.forms import diagrama_secuencia_form, asociacion_form, roles_form

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

class dsCreate(CreateView):
	model = diagrama_secuencia
	form_class = diagrama_secuencia_form
	template_name = 'analisis/ds_form.html'
	success_url = reverse_lazy('analisis:listar_ds')

class dsList(ListView):
	model = diagrama_secuencia
	template_name = 'analisis/ds_list.html'
	paginate_by = 5

class dsEdit(UpdateView):
	model = diagrama_secuencia
	form_class = diagrama_secuencia_form
	template_name = 'analisis/ds_form.html'
	success_url = reverse_lazy('analisis:listar_ds')

class dsDelete(DeleteView):
	model = diagrama_secuencia
	template_name = 'analisis/ds_delete.html'
	success_url = reverse_lazy('analisis:listar_ds')

# asociacion 


class asoCreate(CreateView):
	model = asociacion
	form_class = asociacion_form
	template_name = 'analisis/aso_form.html'
	success_url = reverse_lazy('analisis:listar_aso')

class asoList(ListView):
	model = asociacion
	template_name = 'analisis/aso_list.html'
	paginate_by = 5

class asoEdit(UpdateView):
	model = asociacion
	form_class = asociacion_form
	template_name = 'analisis/aso_form.html'
	success_url = reverse_lazy('analisis:listar_aso')

class asoDelete(DeleteView):
	model = asociacion
	template_name = 'analisis/aso_delete.html'
	success_url = reverse_lazy('analisis:listar_aso')

# roles 

class rolesCreate(CreateView):
	model = roles
	form_class = roles_form
	template_name = 'analisis/roles_form.html'
	success_url = reverse_lazy('analisis:listar_roles')

class rolesList(ListView):
	model = roles
	template_name = 'analisis/roles_list.html'
	paginate_by = 5

class rolesEdit(UpdateView):
	model = roles
	form_class = roles_form
	template_name = 'analisis/roles_form.html'
	success_url = reverse_lazy('analisis:listar_roles')

class rolesDelete(DeleteView):
	model = roles
	template_name = 'analisis/roles_delete.html'
	success_url = reverse_lazy('analisis:listar_roles')