from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from apps.usuario.views import RegistroUsuario, usuario_view, index, userList, userCreate, \
userUpdate, userDelete

from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# from apps.usuario.views import RegistroUsuario, UserAPI

urlpatterns = [
	url(r'^$', login_required(index), name='index'),
	url(r'^login/$', login_required(auth_views.login), {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', login_required(auth_views.logout), name='logout'),

	url(r'^nuevo_user/$', login_required(userCreate.as_view()), name='user_crear'),
    url(r'^listar_user/$', login_required(userList.as_view()), name='user_listar'),
    url(r'^editar_user/(?P<pk>\d+)/$', login_required(userUpdate.as_view()), name='user_editar'),
    url(r'^eliminar_user/(?P<pk>\d+)/$', login_required(userDelete.as_view()), name='user_eliminar'),
	# url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
	url(r'^nuevo/$', usuario_view, name="registrar_user"),
	# url(r'^api', UserAPI.as_view(), name="api"),

]
