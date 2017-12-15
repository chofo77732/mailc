# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from apps.projecto.models import Projecto
# Create your models here.

class diagrama_secuencia(models.Model):

	nombre = models.CharField(max_length=50)
	diagrama = models.FileField(null=True, blank=True)
	descripcion = models.TextField()
	comentario = models.TextField()
	fecha_creacion = models.DateTimeField ( auto_now = False , auto_now_add = True)
	fecha_actualizacion = models.DateTimeField ( auto_now = True , auto_now_add = False)
	projecto = models.ForeignKey(Projecto, null=False, blank=False, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)

class asociacion(models.Model):

	nombre = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
	requisitos = models.TextField()
	descripcion = models.TextField()
	comentario = models.TextField()
	fecha_creacion = models.DateTimeField ( auto_now = False , auto_now_add = True)
	fecha_actualizacion = models.DateTimeField ( auto_now = True , auto_now_add = False)
	projecto = models.ForeignKey(Projecto, null=False, blank=False, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)

class roles(models.Model):

	nombre = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)
	multiplicidad = models.TextField()
	descripcion = models.TextField()
	comentario = models.TextField()
	fecha_creacion = models.DateTimeField ( auto_now = False , auto_now_add = True)
	fecha_actualizacion = models.DateTimeField ( auto_now = True , auto_now_add = False)
	projecto = models.ForeignKey(Projecto, null=False, blank=False, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)

