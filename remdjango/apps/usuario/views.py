# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.shortcuts import render, redirect

# Create your views here.
import json
from rest_framework.views import APIView

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from apps.usuario.forms import RegistroForm
from apps.usuario.serializers import UserSerializer

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registro.html"
	form_class = RegistroForm
	success_url = reverse_lazy('proyecto')

def index(request):
	# return HttpResponse("Hola Mundo")
	return render (request, 'projecto/index.html')

def usuario_view(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('proyecto:proyecto_listar')
	else:
		form = RegistroForm()
	return render(request, 'inicio.html', {'usuario':form})


# class UserAPI(APIView):
# 	serializer = UserSerializer

# 	def get(self, request, format=None):
# 		lista = User.objects.all()
# 		response = self.serializer(lista, many=True)

# 		return HttpResponse(json.dumps(response.data), content_type='application/json')

class userList(ListView):
	model = User
	template_name = 'usuario/participantes.html'
	paginate_by = 5

class userCreate(CreateView):
	model = User
	form_class = RegistroForm
	template_name = 'usuario/par_form.html'
	success_url = reverse_lazy('usuario:user_listar')

class userUpdate(UpdateView):
	model = User
	form_class = RegistroForm
	template_name = 'usuario/par_form.html'
	success_url = reverse_lazy('usuario:user_listar')

class userDelete(DeleteView):
	model = User
	template_name = 'usuario/par_delete.html'
	success_url = reverse_lazy('usuario:user_listar')
