from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
	name = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)



class Estado(models.Model):
	estado = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)
	contexto = models.CharField(max_length=100)

	def __unicode__(self):
		return self.estado


#### Cursos
class Modalidad(models.Model):
	modalidad = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.modalidad

class Curso(models.Model):
	nombre = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)
	moodle_course = models.ForeignKey('moodle.Curso')
	modalidad = models.ForeignKey(Modalidad)

	def __unicode__(self):
		return self.curso

class ProductoModalidadCurso(models.Model):
	curso = models.ForeignKey(Curso)
	producto = models.ForeignKey('ecommerce.Producto')
	habilitado = models.BooleanField(default=True)

class Periodo(models.Model):
	clave = models.CharField(max_length=100)
	inicio = models.DateTimeField()
	fin = models.DateTimeField()
	
	def __unicode__(self):
		return self.clave

class PeriodoCurso(models.Model):
	periodo = models.ForeignKey(Periodo)
	curso = models.ForeignKey(Curso)
	habilitado = models.BooleanField(default=True)


class Grupo(models.Model):
	periodocurso = models.ForeignKey(PeriodoCurso)
	clave = models.CharField(max_length=10)
	nombre = models.CharField(max_length=100)
	min_alumnos = models.IntegerField()
	max_alumnos = models.IntegerField()
	alumnos = models.ManyToManyField(User, trough='GrupoAlumno')
	habilitado = models.BooleanField(default=True)
	grupo_moodle = models.ForeignKey('moodle.Grupo')


class GrupoAlumno(models.Model):
	grupo = models.ForeignKey(Grupo)
	alumno = models.ForeignKey(User)

#### Inscripcion


class Inscripcion(models.Model):
	usuario = models.ForeignKey(User)
	periodocurso = models.ForeignKey(PeriodoCurso)
	estado = models.ForeignKey(Estado)


class InscripcionOrden(models.Model):
	inscripcion = models.ForeignKey(Inscripcion)
	orden = models.ForeignKey('ecommerce.OrdenCompra')


#### Documentos
class TipoDocumento(models.Model):
	tipo = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.tipo

class Documento(models.Model):
	documento = models.CharField(max_length=100)
	tipo_documento = models.ForeignKey(TipoDocumento)
	habilitado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.documento

class DocumentoCurso(models.Model):
	modalidadcurso = models.ForeignKey(ModalidadCurso)
	documento = models.ForeignKey(Documento)
	habilitado = models.BooleanField(default=True)

class DocumentoInscripcion(models.Model):
	inscripcion = models.ForeignKey(Inscripcion)
	documento = models.ForeignKey(Documento)
	estado = models.ForeignKey(Estado)



#### Datos Personales

class ReferenciaPersonal(models.Model):
	nombre = models.CharField(max_length=100)
	apellido_materno = models.CharField(max_length=100)
	apellido_paterno = models.CharField(max_length=100)
	email = models.CharField(max_length=100, null=True)
	lada_local = models.CharField(max_length=10, null=True)
	telefono_local = models.CharField(max_length=15, null=True)
	lada_movil = models.CharField(max_length=10, null=True)
	telefono_movil = models.CharField(max_length=15, null=True)
	parentesco = models.CharField(max_length=100)
	user = models.ForeignKey(User)

class DatosPersonales(models.Model):
	genero = models.CharField(max_length=25)
	edad = models.IntegerField()
	curp = models.CharField(max_length=20, null=True)
	fecha_nacimiento = models.DateTimeField()
	lada_local = models.CharField(max_length=10, null=True)
	telefono_local = models.CharField(max_length=15, null=True)
	lada_movil = models.CharField(max_length=10, null=True)
	telefono_movil = models.CharField(max_length=15, null=True)
	referencia = models.ForeignKey(ReferenciaPersonal)
	id_moodle = models.IntegerField()
	usuario = models.ForeignKey(User)




#### E-commerce

class FormaPagoCurso(models.Model):
	
	forma_pago = models.ForeignKey('ecommerce.FormaPago')
	curso = models.ForeignKey(Curso)
	habilitado = models.BooleanField(default=True)

#Solicitud de admisión


class SolicitudAdmision(models.Model):
	estado = models.ForeignKey(Estado)
	usuario = models.ForeignKey(User)
	periodocurso = models.ForeignKey(PeriodoCurso)