from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.requisitos.views import  index, actorCreate, actorList, actorEdit, actorDelete,\
objetivoCreate, objetivoList, objetivoEdit, objetivoDelete, queryRequisitos, riCreate, riList, \
riEdit, riDelete, rrCreate, rrList, rrEdit, rrDelete, cuCreate, cuList, cuEdit, cuDelete, \
rfCreate, rfList, rfEdit, rfDelete, rnfCreate, rnfList, rnfEdit, rnfDelete, matrizCreate, \
matrizList, matrizEdit, matrizDelete, some_view, generate_PDF, render_pdf_view

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
    # urls actor
    url(r'^nuevo_actor$', login_required(actorCreate.as_view()), name='nuevo_actor'),
    url(r'^listar_actor', login_required(actorList.as_view()), name='listar_actor'),
    url(r'^editar_actor/(?P<pk>\d+)/$', login_required(actorEdit.as_view()), name='editar_actor'),
    url(r'^eliminar_actor/(?P<pk>\d+)/$', login_required(actorDelete.as_view()), name='eliminar_actor'),
    # urls objetivos
    url(r'^nuevo_obj$', login_required(objetivoCreate.as_view()), name='nuevo_objetivo'),
    url(r'^listar_obj', login_required(objetivoList.as_view()), name='listar_objetivo'),
    url(r'^editar_obj/(?P<pk>\d+)/$', login_required(objetivoEdit.as_view()), name='editar_objetivo'),
    url(r'^eliminar_obj/(?P<pk>\d+)/$', login_required(objetivoDelete.as_view()), name='eliminar_objetivo'),
    #urls requisitos de informacion
    url(r'^nuevo_req_inf$', login_required(riCreate.as_view()), name='nuevo_ri'),
    url(r'^listar_req_inf', login_required(riList.as_view()), name='listar_ri'),
    url(r'^editar_req_inf/(?P<pk>\d+)/$', login_required(riEdit.as_view()), name='editar_ri'),
    url(r'^eliminar_req_inf/(?P<pk>\d+)/$', login_required(riDelete.as_view()), name='eliminar_ri'),
    #urls requisitos de informacion
    url(r'^nuevo_req_rr$', login_required(rrCreate.as_view()), name='nuevo_rr'),
    url(r'^listar_req_rr', login_required(rrList.as_view()), name='listar_rr'),
    url(r'^editar_req_rr/(?P<pk>\d+)/$', login_required(rrEdit.as_view()), name='editar_rr'),
    url(r'^eliminar_req_rr/(?P<pk>\d+)/$', login_required(rrDelete.as_view()), name='eliminar_rr'),
    #urls caso de uso
    url(r'^nuevo_cu$', login_required(cuCreate.as_view()), name='nuevo_cu'),
    url(r'^listar_cu', login_required(cuList.as_view()), name='listar_cu'),
    url(r'^editar_cu/(?P<pk>\d+)/$', login_required(cuEdit.as_view()), name='editar_cu'),
    url(r'^eliminar_cu/(?P<pk>\d+)/$', login_required(cuDelete.as_view()), name='eliminar_cu'),
    #urls requisito funcional
    url(r'^nuevo_rf$', login_required(rfCreate.as_view()), name='nuevo_rf'),
    url(r'^listar_rf', login_required(rfList.as_view()), name='listar_rf'),
    url(r'^editar_rf/(?P<pk>\d+)/$', login_required(rfEdit.as_view()), name='editar_rf'),
    url(r'^eliminar_rf/(?P<pk>\d+)/$', login_required(rfDelete.as_view()), name='eliminar_rf'),
    #urls requisito no funcional
    url(r'^nuevo_rnf$', login_required(rnfCreate.as_view()), name='nuevo_rnf'),
    url(r'^listar_rnf', login_required(rnfList.as_view()), name='listar_rnf'),
    url(r'^editar_rnf/(?P<pk>\d+)/$', login_required(rnfEdit.as_view()), name='editar_rnf'),
    url(r'^eliminar_rnf/(?P<pk>\d+)/$', login_required(rnfDelete.as_view()), name='eliminar_rnf'),
    #urls Matriz
    url(r'^nuevo_matriz$', login_required(matrizCreate.as_view()), name='nuevo_matriz'),
    url(r'^listar_matriz', login_required(matrizList.as_view()), name='listar_matriz'),
    url(r'^editar_matriz/(?P<pk>\d+)/$', login_required(matrizEdit.as_view()), name='editar_matriz'),
    url(r'^eliminar_matriz/(?P<pk>\d+)/$', login_required(matrizDelete.as_view()), name='eliminar_matriz'),

    url(r'^tabla', login_required(queryRequisitos), name='tabla'),
    url(r'^pdf', login_required(generate_PDF), name='pdf'),

    # url(r'^listar', login_required(ProjectList.as_view()), name='proyecto_listar'),
]
