# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models

# Create your models here.
class Projecto(models.Model):
	nombre = models.CharField(max_length=100)
	version = models.IntegerField()
	fecha = models.DateField(auto_now = False , auto_now_add = True)
	por = models.CharField(max_length=100)
	para = models.CharField(max_length=100)

	def __unicode__(self):
		return '{}'.format(self.nombre)