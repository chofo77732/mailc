# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from apps.projecto.models import Projecto
from apps.requisitos.models import objetivo, actor

# Create your models here.

class conflicto(models.Model):
	requisito_choices= (
		('PD','PD'),
		('Importante','Importante'),
		('Vital','Vital'),
		)
	nombre = models.CharField(max_length=50)
	version = models.CharField(max_length=50)
	fuentes = models.CharField(max_length=100)
	autores = models.ManyToManyField(actor, blank=True)
	conflicto_obj = models.ManyToManyField(objetivo, blank=True)
	requerimiento = models.TextField()
	descripcion = models.TextField()
	solucion_alt = models.TextField()
	solucion = models.TextField()
	importancia = models.CharField(max_length=15, choices = requisito_choices, default="PD")
	urgencia = models.CharField(max_length=15, choices = requisito_choices, default="PD")
	estado = models.CharField(max_length=15, choices = requisito_choices, default="PD")
	estabilidad = models.CharField(max_length=15, choices = requisito_choices, default="PD")
	comentario = models.TextField()
	fecha_creacion = models.DateTimeField ( auto_now = False , auto_now_add = True)
	fecha_actualizacion = models.DateTimeField ( auto_now = True , auto_now_add = False)
	projecto = models.ForeignKey(Projecto, null=False, blank=False, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)

class defecto(models.Model):
	requisito_choices= (
		('PD','PD'),
		('Importante','Importante'),
		('Vital','Vital'),
		)
	nombre = models.CharField(max_length=50)
	version = models.CharField(max_length=50)
	fuentes = models.CharField(max_length=100)
	autores = models.ManyToManyField(actor, blank=True)
	conflicto_obj = models.ManyToManyField(objetivo, blank=True)
	requerimiento = models.TextField()
	descripcion = models.TextField()
	solucion_alt = models.TextField()
	solucion = models.TextField()
	importancia = models.CharField(max_length=15, choices = requisito_choices, default="PD")
	urgencia = models.CharField(max_length=15, choices = requisito_choices, default="PD")
	estado = models.CharField(max_length=15, choices = requisito_choices, default="PD")
	estabilidad = models.CharField(max_length=15, choices = requisito_choices, default="PD")
	comentario = models.TextField()
	fecha_creacion = models.DateTimeField ( auto_now = False , auto_now_add = True)
	fecha_actualizacion = models.DateTimeField ( auto_now = True , auto_now_add = False)
	projecto = models.ForeignKey(Projecto, null=False, blank=False, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)