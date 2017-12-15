from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.cambios.views import cambioCreate, cambioList, cambioEdit, cambioDelete

urlpatterns = [
    url(r'^nuevo_cambio/$', login_required(cambioCreate.as_view()), name='crear_cambio'),
    url(r'^listar_cambio/$', login_required(cambioList.as_view()), name='listar_cambio'),
    url(r'^editar_cambio/(?P<pk>\d+)/$', login_required(cambioEdit.as_view()), name='editar_cambio'),
    url(r'^eliminar_cambio/(?P<pk>\d+)/$', login_required(cambioDelete.as_view()), name='eliminar_cambio'),
    

]
