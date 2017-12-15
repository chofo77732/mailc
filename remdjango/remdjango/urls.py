"""remdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from apps.usuario.views import RegistroUsuario, usuario_view, index
from apps.requisitos.views import index as index_requisitos
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    # url(r'^inicio/$', auth_views.logout, {'template_name': 'projecto/index.html'}, name='inicio'),

    url(r'^proyecto/', include('apps.projecto.urls', namespace='proyecto')),
    url(r'^requisitos/', include('apps.requisitos.urls', namespace='requisitos')),
    url(r'^analisis/', include('apps.analisis.urls', namespace='analisis')),
    url(r'^conflictos/', include('apps.conflictos.urls', namespace='conflictos')),
    url(r'^cambios/', include('apps.cambios.urls', namespace='cambios')),
    url(r'^usuario/', include('apps.usuario.urls', namespace='usuario')),
    url(r'^accounts/login/', login, {'template_name':'redirect.html'}, name='aclogin'),
    # url(r'^', login, {'template_name':'index.html'}, name='login'),
    # url(r'^login', login, {'template_name':'index.html'}, name='login'),
    # url(r'^', index, name="index"),
    url(r'^accounts/login/', login, {'template_name':'login.html'}, name='login'),
    url(r'^', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)