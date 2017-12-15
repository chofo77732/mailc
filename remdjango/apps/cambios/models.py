# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from apps.projecto.models import Projecto
from apps.requisitos.models import actor

# Create your models here.

class cambio(models.Model):
	nombre = models.CharField(max_length=50)
	version = models.CharField(max_length=50)
	referencia = models.CharField(max_length=150)
	responsable = models.ManyToManyField(actor, blank=True)
	revisado_por = models.CharField(max_length=150)
	fecha_revision = models.DateTimeField ()
	aprovado_por = models.CharField(max_length=150)
	fecha_aprovacion = models.DateTimeField ()
	proponente = models.CharField(max_length=150)
	cambio = models.TextField()
	descripcion = models.TextField()
	fecha_creacion = models.DateTimeField ( auto_now = False , auto_now_add = True)
	fecha_actualizacion = models.DateTimeField ( auto_now = True , auto_now_add = False)
	comentario = models.TextField()
	projecto = models.ForeignKey(Projecto, null=False, blank=False, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)