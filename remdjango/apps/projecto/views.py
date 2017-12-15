# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.shortcuts import render
from apps.projecto.models import Projecto
from apps.projecto.forms import ProjectoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from apps.analisis.models import diagrama_secuencia, asociacion, roles

from apps.requisitos.models import actor, objetivo, requisito_informacion, requisito_restriccion, \
caso_uso, requisito_funcional, requisito_no_funcional, matriz

from apps.conflictos.models import conflicto, defecto
from apps.cambios.models import cambio
# Create your views here.

import os
from django.conf import settings
from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from xhtml2pdf import pisa 


def query(id_proyecto):
	pro = Projecto.objects.get(id=id_proyecto)
	actores = actor.objects.filter(projecto=id_proyecto)
	objetivos = objetivo.objects.filter(projecto=id_proyecto)
	informacion = requisito_informacion.objects.filter(projecto=id_proyecto)
	restriccion = requisito_restriccion.objects.filter(projecto=id_proyecto)
	uso = caso_uso.objects.filter(projecto=id_proyecto)
	funcional = requisito_funcional.objects.filter(projecto=id_proyecto)
	nofuncional = requisito_no_funcional.objects.filter(projecto=id_proyecto)
	matrices = matriz.objects.filter(projecto=id_proyecto)

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

def render_pdf_view(request, id_proyecto):
    template_path = 'requisitos/table.html'
    # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ReporteRequisitos.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(dict(query(id_proyecto)))

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdfRequisitos(request, id_proyecto):
	pro = Projecto.objects.get(id=id_proyecto)
	actores = actor.objects.filter(projecto=id_proyecto)
	objetivos = objetivo.objects.filter(projecto=id_proyecto)
	informacion = requisito_informacion.objects.filter(projecto=id_proyecto)
	restriccion = requisito_restriccion.objects.filter(projecto=id_proyecto)
	uso = caso_uso.objects.filter(projecto=id_proyecto)
	funcional = requisito_funcional.objects.filter(projecto=id_proyecto)
	nofuncional = requisito_no_funcional.objects.filter(projecto=id_proyecto)
	matrices = matriz.objects.filter(projecto=id_proyecto)

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
	return render(request, 'projecto/tableRequisitos.html', contexto)

# pdf analisis

def queryAnalisis(id_proyecto):
	pro = Projecto.objects.get(id=id_proyecto)
	secuencia = diagrama_secuencia.objects.filter(projecto=id_proyecto)
	asoc = asociacion.objects.filter(projecto=id_proyecto)
	roll = roles.objects.filter(projecto=id_proyecto)

	contexto = {'proyecto': pro,
				'ds': secuencia,
				'aso': asoc,
				'rol': roll,
				}
	return contexto

def renderAnalisis(request, id_proyecto):
    template_path = 'analisis/table.html'
    # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ReporteAnalisis.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(dict(queryAnalisis(id_proyecto)))

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdfAnalisis(request, id_proyecto):
	pro = Projecto.objects.get(id=id_proyecto)
	secuencia = diagrama_secuencia.objects.filter(projecto=id_proyecto)
	asoc = asociacion.objects.filter(projecto=id_proyecto)
	roll = roles.objects.filter(projecto=id_proyecto)

	contexto = {'proyecto': pro,
				'ds': secuencia,
				'aso': asoc,
				'rol': roll,
				}
	return render(request, 'projecto/tableAnalisis.html', contexto)

# Conflictos y defectos

def queryconflictos(id_proyecto):
	pro = Projecto.objects.get(id=id_proyecto)
	confli = conflicto.objects.filter(projecto=id_proyecto)
	defec = defecto.objects.filter(projecto=id_proyecto)

	contexto = {'proyecto': pro,
				'con': confli,
				'def': defec,
				}
	return contexto

def renderConflictos(request, id_proyecto):
    template_path = 'conflictos/table.html'
    # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ReporteConflictosYDefectos.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(dict(queryconflictos(id_proyecto)))

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdfConflictos(request, id_proyecto):
	pro = Projecto.objects.get(id=id_proyecto)
	confli = conflicto.objects.filter(projecto=id_proyecto)
	defec = defecto.objects.filter(projecto=id_proyecto)

	contexto = {'proyecto': pro,
				'con': confli,
				'def': defec,
				}
	return render(request, 'projecto/tableConflictos.html', contexto)

# Cambios

def queryCambio(id_proyecto):
	pro = Projecto.objects.get(id=id_proyecto)
	change = cambio.objects.filter(projecto=id_proyecto)

	contexto = {'proyecto': pro,
				'cam': change,
				}
	return contexto

def renderCambio(request, id_proyecto):
    template_path = 'cambios/table.html'
    # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ReportePetCambios.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(dict(queryCambio(id_proyecto)))

    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdfCambio(request, id_proyecto):
	pro = Projecto.objects.get(id=id_proyecto)
	change = cambio.objects.filter(projecto=id_proyecto)

	contexto = {'proyecto': pro,
				'cam': change,
				}
	return render(request, 'projecto/tableCambio.html', contexto)


def index(request):
	# return HttpResponse("Hola Mundo")
	return render (request, 'projecto/index.html')

class ProjectList(ListView):
	model = Projecto
	template_name = 'projecto/projecto_list.html'
	paginate_by = 5

class ProjectCreate(CreateView):
	model = Projecto
	form_class = ProjectoForm
	template_name = 'projecto/projecto_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')

class ProjectUpdate(UpdateView):
	model = Projecto
	form_class = ProjectoForm
	template_name = 'projecto/projecto_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')

class ProjectDelete(DeleteView):
	model = Projecto
	template_name = 'projecto/projecto_delete.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')
