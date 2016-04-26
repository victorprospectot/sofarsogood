# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	id_moodle = models.IntegerField(null=True)
	nombre = models.CharField(max_length=25)
	habilitado = models.BooleanField(default=True)
	idnumber = models.CharField(max_length=25, null=True)
	descripcion = models.TextField()

class CatalogoModoGrupos(models.Model):

	SEPARATE = 1
	
	id_moodle = models.IntegerField()
	tipo = models.CharField(max_length=10)
	habilitado = models.BooleanField(default=True)

class Curso(models.Model):
	fullname = models.CharField(max_length=100)
	shortname = models.CharField(max_length=50)
	idnumber = models.CharField(max_length=50, null=True)
	categoria = models.ForeignKey(Categoria)
	summary = models.CharField(max_length=100, null=True)
	format = models.CharField(max_length=20, default="weeks")
	startdate = models.DateTimeField(null=True)
	groupmode = models.ForeignKey(CatalogoModoGrupos, default=CatalogoModoGrupos.SEPARATE)
	groupmodeforce = models.IntegerField(default=1)
	numsections = models.IntegerField(default=1)
	id_moodle = models.IntegerField(null=True)
	habilitado = models.BooleanField(default=True)

class Grupo(models.Model):
	id_moodle = models.IntegerField(null=True)
	curso = models.ForeignKey(Curso)
	habilitado = models.BooleanField(default=True)
	name = models.CharField(max_length=100)
	descripcion = models.TextField()
	alumnos = models.ManyToManyField(User, through='GrupoUsuario')
