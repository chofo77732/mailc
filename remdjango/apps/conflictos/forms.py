# -*- encoding:utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django import forms

from apps.conflictos.models import conflicto, defecto



class conflictoForm(forms.ModelForm):

	class Meta:
		model = conflicto
		fields = [
			'nombre',
			'version',
			'fuentes',
			'autores',
			'conflicto_obj',
			'requerimiento',
			'descripcion',
			'solucion_alt',
			'solucion',
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
			'conflicto_obj': 'Objetivos',
			'requerimiento': 'requerimiento',
			'descripcion': 'descripcion',
			'solucion_alt': 'solucion alternativa',
			'solucion': 'solucion',
			'importancia': 'importancia',
			'urgencia': 'urgencia',
			'estado': 'estado',
			'estabilidad': 'estabilidad',
			'comentario': 'comentario',
			'projecto': 'projecto',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'version':forms.TextInput(attrs={'class':'form-control'}),
			'fuentes':forms.TextInput(attrs={'class':'form-control'}),
			'autores':forms.SelectMultiple(attrs={'class':'form-control'}),
			'conflicto_obj':forms.SelectMultiple(attrs={'class':'form-control'}),
			'requerimiento':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'solucion_alt':forms.TextInput(attrs={'class':'form-control'}),
			'solucion':forms.TextInput(attrs={'class':'form-control'}),
			'importancia':forms.Select(attrs={'class':'form-control'}),
			'urgencia':forms.Select(attrs={'class':'form-control'}),
			'estado':forms.Select(attrs={'class':'form-control'}),
			'estabilidad':forms.Select(attrs={'class':'form-control'}),
			'comentario':forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}

class defectoForm(forms.ModelForm):

	class Meta:
		model = defecto
		fields = [
			'nombre',
			'version',
			'fuentes',
			'autores',
			'conflicto_obj',
			'requerimiento',
			'descripcion',
			'solucion_alt',
			'solucion',
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
			'conflicto_obj': 'Objetivos',
			'requerimiento': 'requerimiento',
			'descripcion': 'descripcion',
			'solucion_alt': 'solucion alternativa',
			'solucion': 'solucion',
			'importancia': 'importancia',
			'urgencia': 'urgencia',
			'estado': 'estado',
			'estabilidad': 'estabilidad',
			'comentario': 'comentario',
			'projecto': 'projecto',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'version':forms.TextInput(attrs={'class':'form-control'}),
			'fuentes':forms.TextInput(attrs={'class':'form-control'}),
			'autores':forms.SelectMultiple(attrs={'class':'form-control'}),
			'conflicto_obj':forms.SelectMultiple(attrs={'class':'form-control'}),
			'requerimiento':forms.TextInput(attrs={'class':'form-control'}),
			'descripcion':forms.TextInput(attrs={'class':'form-control'}),
			'solucion_alt':forms.TextInput(attrs={'class':'form-control'}),
			'solucion':forms.TextInput(attrs={'class':'form-control'}),
			'importancia':forms.Select(attrs={'class':'form-control'}),
			'urgencia':forms.Select(attrs={'class':'form-control'}),
			'estado':forms.Select(attrs={'class':'form-control'}),
			'estabilidad':forms.Select(attrs={'class':'form-control'}),
			'comentario':forms.Textarea(attrs={'class':'form-control'}),
			'projecto': forms.Select(attrs={'class':'form-control'}),
		}