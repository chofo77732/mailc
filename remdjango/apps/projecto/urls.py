from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.projecto.views import ProjectList, ProjectCreate, index, ProjectUpdate, ProjectDelete, \
pdfRequisitos, render_pdf_view, renderAnalisis, pdfAnalisis, renderConflictos, pdfConflictos, \
renderCambio, pdfCambio

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^nuevo$', login_required(ProjectCreate.as_view()), name='proyecto_crear'),
    # url(r'^listar', login_required(ProjectList.as_view()), name='proyecto_listar'),
    # url(r'^editar/(?P<pk>\d+)/$', login_required(ProjectUpdate.as_view()), name='proyecto_editar'),
    # url(r'^eliminar/(?P<pk>\d+)/$', login_required(ProjectDelete.as_view()), name='proyecto_eliminar'),
    url(r'^nuevo$', login_required(ProjectCreate.as_view()), name='proyecto_crear'),
    url(r'^listar', login_required(ProjectList.as_view()), name='proyecto_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(ProjectUpdate.as_view()), name='proyecto_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(ProjectDelete.as_view()), name='proyecto_eliminar'),
    url(r'^pdf/(?P<id_proyecto>\d+)/$', login_required(pdfRequisitos), name='pdf'),
    url(r'^descargar_pdf/(?P<id_proyecto>\d+)/$', login_required(render_pdf_view), name='descargar_pdf'),

    url(r'^pdf_ana/(?P<id_proyecto>\d+)/$', login_required(pdfAnalisis), name='pdf_ana'),
    url(r'^descargar_pdf_ana/(?P<id_proyecto>\d+)/$', login_required(renderAnalisis), name='descargar_pdf_ana'),

    url(r'^pdf_con/(?P<id_proyecto>\d+)/$', login_required(pdfConflictos), name='pdf_con'),
    url(r'^descargar_pdf_con/(?P<id_proyecto>\d+)/$', login_required(renderConflictos), name='descargar_pdf_con'),

    url(r'^pdf_cam/(?P<id_proyecto>\d+)/$', login_required(pdfCambio), name='pdf_cam'),
    url(r'^descargar_pdf_cam/(?P<id_proyecto>\d+)/$', login_required(renderCambio), name='descargar_pdf_cam'),


]
