from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TipoFacturacion(models.Model):
	POR_PAGO = 1
	DEVENGAMIENTO = 1
	tipo = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)


class Factura(models.Model):
	pago = models.ForeignKey('ecommerce.Pago')
	tipo = models.ForeignKey(TipoFacturacion)