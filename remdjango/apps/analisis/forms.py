# -*- encoding:utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django import forms

from apps.analisis.models import diagrama_secuencia, asociacion, roles

class diagrama_secuencia_form(forms.ModelForm):

	class Meta:
		model = diagrama_secuencia
		fields = [
			'nombre',
			'diagrama',
			'descripcion',
			'comentario',
			'projecto',
		]
		labels = {
			'nombre': 'nombre',
			'diagrama': 'diagrama',
			'descripcion': 'descripcion',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'diagrama':forms.FileInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'comentario':forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class asociacion_form(forms.ModelForm):

	class Meta:
		model = asociacion
		fields = [
			'nombre',
			'tipo',
			'requisitos',
			'descripcion',
			'comentario',
			'projecto',
		]
		labels = {
			'nombre': 'nombre',
			'tipo': 'tipo',
			'requisitos': 'requisitos',
			'descripcion': 'descripcion',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'tipo':forms.TextInput(attrs={'class':'form-control'}),
			'requisitos':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'comentario':forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class roles_form(forms.ModelForm):

	class Meta:
		model = roles
		fields = [
			'nombre',
			'tipo',
			'multiplicidad',
			'descripcion',
			'comentario',
			'projecto',
		]
		labels = {
			'nombre': 'nombre',
			'tipo': 'tipo',
			'multiplicidad': 'multiplicidad',
			'descripcion': 'descripcion',
			'comentario': 'comentario',
			'projecto': 'projecto',

		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'tipo':forms.TextInput(attrs={'class':'form-control'}),
			'multiplicidad':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'comentario':forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}