from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.analisis.views import dsCreate, dsList, dsEdit, dsDelete, asoCreate, asoList, asoEdit, \
asoDelete, rolesCreate, rolesList, rolesEdit, rolesDelete

urlpatterns = [
    url(r'^nuevo_ds/$', login_required(dsCreate.as_view()), name='crear_ds'),
    url(r'^listar_ds/$', login_required(dsList.as_view()), name='listar_ds'),
    url(r'^editar_ds/(?P<pk>\d+)/$', login_required(dsEdit.as_view()), name='editar_ds'),
    url(r'^eliminar_ds/(?P<pk>\d+)/$', login_required(dsDelete.as_view()), name='eliminar_ds'),
    # urls asociacion
    url(r'^nuevo_aso/$', login_required(asoCreate.as_view()), name='crear_aso'),
    url(r'^listar_aso/$', login_required(asoList.as_view()), name='listar_aso'),
    url(r'^editar_aso/(?P<pk>\d+)/$', login_required(asoEdit.as_view()), name='editar_aso'),
    url(r'^eliminar_aso/(?P<pk>\d+)/$', login_required(asoDelete.as_view()), name='eliminar_aso'),
    # urls roles
    url(r'^nuevo_roles/$', login_required(rolesCreate.as_view()), name='crear_roles'),
    url(r'^listar_roles/$', login_required(rolesList.as_view()), name='listar_roles'),
    url(r'^editar_roles/(?P<pk>\d+)/$', login_required(rolesEdit.as_view()), name='editar_roles'),
    url(r'^eliminar_roles/(?P<pk>\d+)/$', login_required(rolesDelete.as_view()), name='eliminar_roles'),


]
