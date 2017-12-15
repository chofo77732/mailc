# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from apps.projecto.models import Projecto

class actor(models.Model):
	nombre = models.CharField(max_length=50)
	version = models.IntegerField()
	fuentes = models.CharField(max_length=100)
	descripcion = models.TextField()
	comentario = models.TextField()
	fecha_creacion = models.DateTimeField ( auto_now = False , auto_now_add = True)
	fecha_actualizacion = models.DateTimeField ( auto_now = True , auto_now_add = False)
	projecto = models.ForeignKey(Projecto, null=False, blank=False, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)

class objetivo(models.Model):
	objetivo_choices= (
		('PD','PD'),
		('Importante','Importante'),
		('Vital','Vital'),
		)
	nombre = models.CharField(max_length=50)
	version = models.IntegerField()
	fuentes = models.CharField(max_length=100)
	autores = models.ManyToManyField(actor, blank=True)
	descripcion = models.TextField()
	importancia = models.CharField(max_length=15, choices = objetivo_choices, default="PD")
	urgencia = models.CharField(max_length=15, choices = objetivo_choices, default="PD")
	estado = models.CharField(max_length=15, choices = objetivo_choices, default="PD")
	estabilidad = models.CharField(max_length=15, choices = objetivo_choices, default="PD")
	comentario = models.TextField()
	fecha_creacion = models.DateTimeField ( auto_now = False , auto_now_add = True)
	fecha_actualizacion = models.DateTimeField ( auto_now = True , auto_now_add = False)
	projecto = models.ForeignKey(Projecto, null=False, blank=False, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)

class requisito_informacion(models.Model):
	requisito_choices= (
		('PD','PD'),
		('Importante','Importante'),
		('Vital','Vital'),
		)
	nombre = models.CharField(max_length=50)
	version = models.IntegerField()
	fuentes = models.CharField(max_length=100)
	autores = models.ManyToManyField(actor, blank=True)
	descripcion = models.TextField()
	dato_especifico = models.TextField()
	tiempo_vida = models.TextField()
	ocurrencia = models.TextField()
	dependencias = models.ManyToManyField(objetivo, blank=True)
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

class requisito_restriccion(models.Model):
	requisito_choices= (
		('PD','PD'),
		('Importante','Importante'),
		('Vital','Vital'),
		)
	nombre = models.CharField(max_length=50)
	version = models.IntegerField()
	fuentes = models.CharField(max_length=100)
	autores = models.ManyToManyField(actor, blank=True)
	descripcion = models.TextField()
	dependencias = models.ManyToManyField(objetivo, blank=True)
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

class caso_uso(models.Model):
	requisito_choices= (
		('PD','PD'),
		('Importante','Importante'),
		('Vital','Vital'),
		)
	nombre = models.CharField(max_length=50)
	version = models.IntegerField()
	fuentes = models.CharField(max_length=100)
	autores = models.ManyToManyField(actor, blank=True)
	descripcion = models.TextField()
	precondicion = models.TextField()
	postcondicion = models.TextField()
	frecuencia = models.TextField()
	dependencias = models.ManyToManyField(objetivo, blank=True)
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

class requisito_funcional(models.Model):
	requisito_choices= (
		('PD','PD'),
		('Importante','Importante'),
		('Vital','Vital'),
		)
	nombre = models.CharField(max_length=50)
	version = models.IntegerField()
	fuentes = models.CharField(max_length=100)
	autores = models.ManyToManyField(actor, blank=True)
	descripcion = models.TextField()
	dependencias = models.ManyToManyField(objetivo, blank=True)
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

class requisito_no_funcional(models.Model):
	requisito_choices= (
		('PD','PD'),
		('Importante','Importante'),
		('Vital','Vital'),
		)
	nombre = models.CharField(max_length=50)
	version = models.IntegerField()
	fuentes = models.CharField(max_length=100)
	autores = models.ManyToManyField(actor, blank=True)
	descripcion = models.TextField()
	dependencias = models.ManyToManyField(objetivo, blank=True)
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

class matriz(models.Model):
	requisito_choices= (
		('requisito_informacion','requisito informacion'),
		('requisito_restriccion','requisito restriccion'),
		('caso_uso','caso de uso'),
		('requisito_funcional','requisito funcional'),
		('requisito_no_funcional','requisito no funcional'),
		)
	nombre = models.CharField(max_length=50)
	version = models.IntegerField()
	fuentes = models.CharField(max_length=100)
	autores = models.ManyToManyField(actor, blank=True)
	trazar = models.CharField(max_length=30, choices = requisito_choices)
	comentario = models.TextField()
	fecha_creacion = models.DateTimeField ( auto_now = False , auto_now_add = True)
	fecha_actualizacion = models.DateTimeField ( auto_now = True , auto_now_add = False)
	projecto = models.ForeignKey(Projecto, null=False, blank=False, on_delete=models.CASCADE)

	def __unicode__(self):
		return '{}'.format(self.nombre)


