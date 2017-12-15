from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.conflictos.views import conCreate, conList, conEdit, conDelete, defCreate, defList, \
defEdit, defDelete

urlpatterns = [
    url(r'^nuevo_con/$', login_required(conCreate.as_view()), name='crear_con'),
    url(r'^listar_con/$', login_required(conList.as_view()), name='listar_con'),
    url(r'^editar_con/(?P<pk>\d+)/$', login_required(conEdit.as_view()), name='editar_con'),
    url(r'^eliminar_con/(?P<pk>\d+)/$', login_required(conDelete.as_view()), name='eliminar_con'),
    # # urls defectos
    url(r'^nuevo_def/$', login_required(defCreate.as_view()), name='crear_def'),
    url(r'^listar_def/$', login_required(defList.as_view()), name='listar_def'),
    url(r'^editar_def/(?P<pk>\d+)/$', login_required(defEdit.as_view()), name='editar_def'),
    url(r'^eliminar_def/(?P<pk>\d+)/$', login_required(defDelete.as_view()), name='eliminar_def'),
    


]
