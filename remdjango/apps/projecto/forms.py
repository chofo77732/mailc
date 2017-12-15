# -*- encoding:utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django import forms

from apps.projecto.models import Projecto



class ProjectoForm(forms.ModelForm):

	class Meta:
		model = Projecto
		fields = [
			'nombre',
			'version',
			'por',
			'para',
		]
		labels = {
			'nombre': 'nombre',
			'version': 'version',
			'por': 'por',
			'para': 'para',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'version':forms.TextInput(attrs={'class':'form-control'}),
			'por':forms.TextInput(attrs={'class':'form-control'}),
			'para':forms.TextInput(attrs={'class':'form-control'}),
		}
