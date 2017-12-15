# -*- encoding:utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django import forms

from apps.cambios.models import cambio



class cambioForm(forms.ModelForm):

	class Meta:
		model = cambio
		fields = [
			'nombre',
			'version',
			'referencia',
			'responsable',
			'revisado_por',
			'fecha_revision',
			'aprovado_por',
			'fecha_aprovacion',
			'proponente',
			'cambio',
			'descripcion',
			'comentario',
			'projecto',
			
		]
		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'referencia': 'referencia',
			'responsable': 'responsable',
			'revisado_por': 'revisado_por',
			'fecha_revision': 'fecha_revision',
			'aprovado_por': 'aprovado_por',
			'fecha_aprovacion': 'fecha_aprovacion alternativa',
			'proponente': 'proponente',
			'cambio': 'cambio',
			'descripcion': 'descripcion',
			'comentario': 'comentario',
			'projecto': 'projecto',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'version':forms.TextInput(attrs={'class':'form-control'}),
			'referencia':forms.TextInput(attrs={'class':'form-control'}),
			'responsable':forms.SelectMultiple(attrs={'class':'form-control'}),
			'revisado_por':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_revision':forms.DateTimeInput(attrs={'class':'form-control'}),
			'aprovado_por':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_aprovacion':forms.DateTimeInput(attrs={'class':'form-control'}),
			'proponente':forms.TextInput(attrs={'class':'form-control'}),
			'cambio':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'comentario':forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}
