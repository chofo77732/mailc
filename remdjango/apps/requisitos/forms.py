# -*- encoding:utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django import forms

from apps.requisitos.models import actor, objetivo, requisito_informacion, requisito_restriccion, \
caso_uso, requisito_funcional, requisito_no_funcional, matriz

class actorForm(forms.ModelForm):

	class Meta:
		model = actor
		fields = [
			'nombre',
			'version',
			'fuentes',
			'descripcion',
			'comentario',
			'projecto',
		]
		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'fuentes': 'fuentes',
			'descripcion': 'descripcion',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'version':forms.TextInput(attrs={'class':'form-control'}),
			'fuentes':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'comentario':forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class objetivoForm(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model = objetivo

		fields = [
			'nombre',
			'version',
			'fuentes',
			'autores',
			'descripcion',
			'importancia',
			'urgencia',
			'estado',
			'estabilidad',
			'comentario',
			'projecto',
		]

		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'fuentes': 'fuentes',
			'autores': 'autores',
			'descripcion': 'descripcion',
			'importancia': 'importancia',
			'urgencia': 'urgencia',
			'estado': 'estado',
			'estabilidad': 'estabilidad',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'fuentes': forms.TextInput(attrs={'class':'form-control'}),
			'autores': forms.SelectMultiple(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'importancia': forms.Select(attrs={'class':'form-control'}),
			'urgencia': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'estabilidad': forms.Select(attrs={'class':'form-control'}),
			'comentario': forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class requisito_informacion_Form(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model = requisito_informacion

		fields = [
			'nombre',
			'version',
			'fuentes',
			'autores',
			'descripcion',
			'dato_especifico',
			'tiempo_vida',
			'ocurrencia',
			'dependencias',
			'importancia',
			'urgencia',
			'estado',
			'estabilidad',
			'comentario',
			'projecto',
		]

		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'fuentes': 'fuentes',
			'autores': 'autores',
			'descripcion': 'descripcion',
			'dato_especifico': 'dato_especifico',
			'tiempo_vida': 'tiempo_vida',
			'ocurrencia': 'ocurrencia',
			'dependencias': 'dependencias',
			'importancia': 'importancia',
			'urgencia': 'urgencia',
			'estado': 'estado',
			'estabilidad': 'estabilidad',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'fuentes': forms.TextInput(attrs={'class':'form-control'}),
			'autores': forms.SelectMultiple(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'dato_especifico': forms.TextInput(attrs={'class':'form-control'}),
			'tiempo_vida': forms.TextInput(attrs={'class':'form-control'}),
			'ocurrencia': forms.TextInput(attrs={'class':'form-control'}),
			'dependencias': forms.SelectMultiple(attrs={'class':'form-control'}),
			'importancia': forms.Select(attrs={'class':'form-control'}),
			'urgencia': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'estabilidad': forms.Select(attrs={'class':'form-control'}),
			'comentario': forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class requisito_restriccion_Form(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model = requisito_restriccion

		fields = [
			'nombre',
			'version',
			'fuentes',
			'autores',
			'descripcion',
			'dependencias',
			'importancia',
			'urgencia',
			'estado',
			'estabilidad',
			'comentario',
			'projecto',
		]

		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'fuentes': 'fuentes',
			'autores': 'autores',
			'descripcion': 'descripcion',
			'dependencias': 'dependencias',
			'importancia': 'importancia',
			'urgencia': 'urgencia',
			'estado': 'estado',
			'estabilidad': 'estabilidad',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'fuentes': forms.TextInput(attrs={'class':'form-control'}),
			'autores': forms.SelectMultiple(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'dependencias': forms.SelectMultiple(attrs={'class':'form-control'}),
			'importancia': forms.Select(attrs={'class':'form-control'}),
			'urgencia': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'estabilidad': forms.Select(attrs={'class':'form-control'}),
			'comentario': forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class caso_uso_Form(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model = caso_uso

		fields = [
			'nombre',
			'version',
			'fuentes',
			'autores',
			'descripcion',
			'precondicion',
			'postcondicion',
			'frecuencia',
			'dependencias',
			'importancia',
			'urgencia',
			'estado',
			'estabilidad',
			'comentario',
			'projecto',
		]

		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'fuentes': 'fuentes',
			'autores': 'autores',
			'descripcion': 'descripcion',
			'precondicion': 'precondicion',
			'postcondicion': 'postcondicion',
			'frecuencia': 'frecuencia',
			'dependencias': 'dependencias',
			'importancia': 'importancia',
			'urgencia': 'urgencia',
			'estado': 'estado',
			'estabilidad': 'estabilidad',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'fuentes': forms.TextInput(attrs={'class':'form-control'}),
			'autores': forms.SelectMultiple(attrs={'class':'form-control'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
			'precondicion': forms.TextInput(attrs={'class':'form-control'}),
			'postcondicion': forms.TextInput(attrs={'class':'form-control'}),
			'frecuencia': forms.TextInput(attrs={'class':'form-control'}),
			'dependencias': forms.SelectMultiple(attrs={'class':'form-control'}),
			'importancia': forms.Select(attrs={'class':'form-control'}),
			'urgencia': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'estabilidad': forms.Select(attrs={'class':'form-control'}),
			'comentario': forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class requisito_funcional_Form(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model = requisito_funcional

		fields = [
			'nombre',
			'version',
			'fuentes',
			'autores',
			'descripcion',
			'dependencias',
			'importancia',
			'urgencia',
			'estado',
			'estabilidad',
			'comentario',
			'projecto',
		]

		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'fuentes': 'fuentes',
			'autores': 'autores',
			'descripcion': 'descripcion',
			'dependencias': 'dependencias',
			'importancia': 'importancia',
			'urgencia': 'urgencia',
			'estado': 'estado',
			'estabilidad': 'estabilidad',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'fuentes': forms.TextInput(attrs={'class':'form-control'}),
			'autores': forms.SelectMultiple(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'dependencias': forms.SelectMultiple(attrs={'class':'form-control'}),
			'importancia': forms.Select(attrs={'class':'form-control'}),
			'urgencia': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'estabilidad': forms.Select(attrs={'class':'form-control'}),
			'comentario': forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class requisito_no_funcional_Form(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model = requisito_no_funcional

		fields = [
			'nombre',
			'version',
			'fuentes',
			'autores',
			'descripcion',
			'dependencias',
			'importancia',
			'urgencia',
			'estado',
			'estabilidad',
			'comentario',
			'projecto',
		]

		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'fuentes': 'fuentes',
			'autores': 'autores',
			'descripcion': 'descripcion',
			'dependencias': 'dependencias',
			'importancia': 'importancia',
			'urgencia': 'urgencia',
			'estado': 'estado',
			'estabilidad': 'estabilidad',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'fuentes': forms.TextInput(attrs={'class':'form-control'}),
			'autores': forms.SelectMultiple(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'dependencias': forms.SelectMultiple(attrs={'class':'form-control'}),
			'importancia': forms.Select(attrs={'class':'form-control'}),
			'urgencia': forms.Select(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
			'estabilidad': forms.Select(attrs={'class':'form-control'}),
			'comentario': forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class matriz_Form(forms.ModelForm):
	"""docstring for MascotaForm"""
	class Meta:
		model = matriz

		fields = [
			'nombre',
			'version',
			'fuentes',
			'autores',
			'trazar',
			'comentario',
			'projecto',
		]

		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'fuentes': 'fuentes',
			'autores': 'autores',
			'trazar': 'trazar',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'version': forms.TextInput(attrs={'class':'form-control'}),
			'fuentes': forms.TextInput(attrs={'class':'form-control'}),
			'autores': forms.SelectMultiple(attrs={'class':'form-control'}),
			'trazar': forms.Select(attrs={'class':'form-control'}),
			'comentario': forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}