# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.shortcuts import render, redirect
from apps.requisitos.models import actor, objetivo, requisito_informacion, requisito_restriccion, \
caso_uso, requisito_funcional, requisito_no_funcional, matriz

from apps.projecto.models import Projecto

from apps.requisitos.forms import actorForm, objetivoForm, requisito_informacion_Form, \
requisito_restriccion_Form, caso_uso_Form, requisito_funcional_Form , requisito_no_funcional_Form, \
matriz_Form

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


def query():
	pro = Projecto.objects.get(id=1)
	actores = actor.objects.filter(projecto=1)
	objetivos = objetivo.objects.filter(projecto=1)
	informacion = requisito_informacion.objects.filter(projecto=1)
	restriccion = requisito_restriccion.objects.filter(projecto=1)
	uso = caso_uso.objects.filter(projecto=1)
	funcional = requisito_funcional.objects.filter(projecto=1)
	nofuncional = requisito_no_funcional.objects.filter(projecto=1)
	matrices = matriz.objects.filter(projecto=1)

	contexto = {'proyecto': pro,
				'actor': actores,
				'obj': objetivos,
				'infor': informacion,
				'res': restriccion,
				'caso': uso,
				'fun': funcional,
				'nofun': nofuncional,
				'mat': matrices,
				}
	return contexto

def generate_PDF(request):

    data = {}

    template = get_template('requisitos/table.html')
    html  = template.render(dict(query()))

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('UTF-8'), dest=file,
            encoding='UTF-8')

    file.seek(0)
    pdf = file.read()
    file.close()     
    return HttpResponse(pdf, 'application/pdf')

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path

def render_pdf_view(request):
    template_path = 'requisitos/table.html'
    # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(dict(query()))

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    template_name = "requisitos/h.html"
    p.drawString(100, 100, "<h1>hola</h1>")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

# Create your views here.
def index(request):
	# return HttpResponse("Hola Mundo")
	return render (request, 'requisitos/index.html')

def queryRequisitos(request):
	pro = Projecto.objects.get(id=1)
	actores = actor.objects.filter(projecto=1)
	objetivos = objetivo.objects.filter(projecto=1)
	informacion = requisito_informacion.objects.filter(projecto=1)
	restriccion = requisito_restriccion.objects.filter(projecto=1)
	uso = caso_uso.objects.filter(projecto=1)
	funcional = requisito_funcional.objects.filter(projecto=1)
	nofuncional = requisito_no_funcional.objects.filter(projecto=1)
	matrices = matriz.objects.filter(projecto=1)

	contexto = {'proyecto': pro,
				'actor': actores,
				'obj': objetivos,
				'infor': informacion,
				'res': restriccion,
				'caso': uso,
				'fun': funcional,
				'nofun': nofuncional,
				'mat': matrices,
				}
	return render(request, 'requisitos/table.html', contexto)


# Actor

class actorCreate(CreateView):
	model = actor
	form_class = actorForm
	template_name = 'requisitos/actor_form.html'
	success_url = reverse_lazy('requisitos:listar_actor')

class actorList(ListView):
	model = actor
	template_name = 'requisitos/actor_list.html'
	paginate_by = 5

class actorEdit(UpdateView):
	model = actor
	form_class = actorForm
	template_name = 'requisitos/actor_form.html'
	success_url = reverse_lazy('requisitos:listar_actor')

class actorDelete(DeleteView):
	model = actor
	template_name = 'requisitos/actor_delete.html'
	success_url = reverse_lazy('requisitos:listar_actor')

#	Objetivo

class objetivoCreate(CreateView):
	model = objetivo
	form_class = objetivoForm
	template_name = 'requisitos/objetivo_form.html'
	success_url = reverse_lazy('requisitos:listar_objetivo')

class objetivoList(ListView):
	model = objetivo
	template_name = 'requisitos/objetivo_list.html'
	paginate_by = 5

class objetivoEdit(UpdateView):
	model = objetivo
	form_class = objetivoForm
	template_name = 'requisitos/objetivo_form.html'
	success_url = reverse_lazy('requisitos:listar_objetivo')

class objetivoDelete(DeleteView):
	model = objetivo
	template_name = 'requisitos/objetivo_delete.html'
	success_url = reverse_lazy('requisitos:listar_objetivo')

# Requisitos de informacion 

class riCreate(CreateView):
	model = requisito_informacion
	form_class = requisito_informacion_Form
	template_name = 'requisitos/ri_form.html'
	success_url = reverse_lazy('requisitos:listar_ri')

class riList(ListView):
	model = requisito_informacion
	template_name = 'requisitos/ri_list.html'
	paginate_by = 5

class riEdit(UpdateView):
	model = requisito_informacion
	form_class = requisito_informacion_Form
	template_name = 'requisitos/ri_form.html'
	success_url = reverse_lazy('requisitos:listar_ri')

class riDelete(DeleteView):
	model = requisito_informacion
	template_name = 'requisitos/ri_delete.html'
	success_url = reverse_lazy('requisitos:listar_ri')

# Requisitos de restriccion 

class rrCreate(CreateView):
	model = requisito_restriccion
	form_class = requisito_restriccion_Form
	template_name = 'requisitos/rr_form.html'
	success_url = reverse_lazy('requisitos:listar_rr')

class rrList(ListView):
	model = requisito_restriccion
	template_name = 'requisitos/rr_list.html'
	paginate_by = 5

class rrEdit(UpdateView):
	model = requisito_restriccion
	form_class = requisito_restriccion_Form
	template_name = 'requisitos/rr_form.html'
	success_url = reverse_lazy('requisitos:listar_rr')

class rrDelete(DeleteView):
	model = requisito_restriccion
	template_name = 'requisitos/rr_delete.html'
	success_url = reverse_lazy('requisitos:listar_rr')

# caso de uso

class cuCreate(CreateView):
	model = caso_uso
	form_class = caso_uso_Form
	template_name = 'requisitos/cu_form.html'
	success_url = reverse_lazy('requisitos:listar_cu')

class cuList(ListView):
	model = caso_uso
	template_name = 'requisitos/cu_list.html'
	paginate_by = 5

class cuEdit(UpdateView):
	model = caso_uso
	form_class = caso_uso_Form
	template_name = 'requisitos/cu_form.html'
	success_url = reverse_lazy('requisitos:listar_cu')

class cuDelete(DeleteView):
	model = caso_uso
	template_name = 'requisitos/cu_delete.html'
	success_url = reverse_lazy('requisitos:listar_cu')

# requisito funcional

class rfCreate(CreateView):
	model = requisito_funcional
	form_class = requisito_funcional_Form
	template_name = 'requisitos/rf_form.html'
	success_url = reverse_lazy('requisitos:listar_rf')

class rfList(ListView):
	model = requisito_funcional
	template_name = 'requisitos/rf_list.html'
	paginate_by = 5

class rfEdit(UpdateView):
	model = requisito_funcional
	form_class = requisito_funcional_Form
	template_name = 'requisitos/rf_form.html'
	success_url = reverse_lazy('requisitos:listar_rf')

class rfDelete(DeleteView):
	model = requisito_funcional
	template_name = 'requisitos/rf_delete.html'
	success_url = reverse_lazy('requisitos:listar_rf')

# requisito no funcional

class rnfCreate(CreateView):
	model = requisito_no_funcional
	form_class = requisito_no_funcional_Form
	template_name = 'requisitos/rnf_form.html'
	success_url = reverse_lazy('requisitos:listar_rnf')

class rnfList(ListView):
	model = requisito_no_funcional
	template_name = 'requisitos/rnf_list.html'
	paginate_by = 5

class rnfEdit(UpdateView):
	model = requisito_no_funcional
	form_class = requisito_no_funcional_Form
	template_name = 'requisitos/rnf_form.html'
	success_url = reverse_lazy('requisitos:listar_rnf')

class rnfDelete(DeleteView):
	model = requisito_no_funcional
	template_name = 'requisitos/rnf_delete.html'
	success_url = reverse_lazy('requisitos:listar_rnf')

# requisito no funcional

class matrizCreate(CreateView):
	model = matriz
	form_class = matriz_Form
	template_name = 'requisitos/matriz_form.html'
	success_url = reverse_lazy('requisitos:listar_matriz')

class matrizList(ListView):
	model = matriz
	template_name = 'requisitos/matriz_list.html'
	paginate_by = 5

class matrizEdit(UpdateView):
	model = matriz
	form_class = matriz_Form
	template_name = 'requisitos/matriz_form.html'
	success_url = reverse_lazy('requisitos:listar_matriz')

class matrizDelete(DeleteView):
	model = matriz
	template_name = 'requisitos/matriz_delete.html'
	success_url = reverse_lazy('requisitos:listar_matriz')