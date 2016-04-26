from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ConfiguracionMoratorios(models.Model):
	dias_despues_vencimiento = models.IntegerField()
	porcentaje_moratorio_mensual = models.IntegerField()

class MoraProducto(models.Model):
	producto = models.ForeignKey('ecommerce.Producto')
	mora = models.ForeignKey(ConfiguracionMoratorios)