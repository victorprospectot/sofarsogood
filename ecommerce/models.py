# -*- coding: utf-8 -*-
from __future__ import unicode_literals


#### Python and third-party libraries
import base64

#### Django Core
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Catalogos

class TipoMovimiento(models.Model):
	tipo = models.CharField(max_length=30)
	clave = models.CharField(max_length=3)
	signo = models.CharField(max_length=1)
	habilitado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.tipo

class Moneda(models.Model):
	divisa = models.CharField(max_length=5)
	moneda = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.divisa

class Impuestos(models.Model):
  tipo_impuesto = models.CharField(max_length=100)
  abreviacion = models.CharField(max_length=10)
  valor = models.DecimalField(max_digits=14, decimal_places=2)
  habilitado = models.BooleanField()
  tipo_movimiento = models.ForeignKey(TipoMovimiento)

  def __unicode__(self):
  	return self.tipo_impuesto + " - " + self.abreviacion

class Producto(models.Model):
	nombre = models.CharField(max_length=100)
	clave = models.CharField(max_length=10)
	moneda = models.ForeignKey(Moneda)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	precio_final = models.DecimalField(max_digits=10, decimal_places=2)
	habilitado = models.BooleanField(default=True)
	valido_hasta = models.DateTimeField(null=True, blank=True)
	#tipo_factura = models.ForeignKey('facturacion.TipoFacturacion', null=True)
	
	def __unicode__(self):
		return self.nombre + " - " + self.clave

class ProductoImpuesto(models.Model):
	impuesto = models.ForeignKey(Impuestos)
	producto = models.ForeignKey(Producto)

class CuponDescuento(models.Model):
  clave_cupon = models.CharField(max_length=10)
  habilitado = models.BooleanField(default=True)
  numero_cupones = models.IntegerField()
  descuento = models.DecimalField(max_digits=10, decimal_places=2)
  porcentaje = models.BooleanField(default=True)
  tipo_movimiento = models.ForeignKey(TipoMovimiento)
  moneda = models.ForeignKey(Moneda, null=True)
  estado = models.ForeignKey('EstadosEcommerce')

  def __unicode__(self):
  	return self.clave_cupon

class Concepto(models.Model):
  nombre = models.CharField(max_length=100)
  habilitado = models.BooleanField(default=True)

################### In other words, in other words, I love you
class EstadosEcommerce(models.Model):
  estado = models.CharField(max_length=100)
  habilitado = models.BooleanField(default=True)
  contexto = models.CharField(max_length=100)

  def __unicode__(self):
    return self.estado


class Cargo(models.Model):
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  fecha_vencimiento = models.DateTimeField()
  producto = models.ForeignKey(Producto)
  tipo_movimiento = models.ForeignKey(TipoMovimiento)
  estado = models.ForeignKey(EstadosEcommerce)


class OrdenCompra(models.Model):
  habilitado = models.BooleanField(default=True)
  usuario = models.ForeignKey(User)
  estado = models.ForeignKey(EstadosEcommerce)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  fecha_vencimiento = models.DateTimeField()
  concepto = models.ForeignKey(Concepto)
  tipo_movimiento = models.ForeignKey(TipoMovimiento)
  cupon = models.ForeignKey(CuponDescuento, null=True)
  cargos = models.ManyToManyField(Cargo, through='CargoOrden')

class CargoOrden(models.Model):
  cargo = models.ForeignKey(Cargo)
  orden = models.ForeignKey(OrdenCompra)



#### Pagos

class FormaPago(models.Model):
	
	PAYPAL = 1
	
	forma_pago = models.CharField(max_length=100)
	habilitado = models.BooleanField(default=True)

	def __unicode__(self):
		return self.forma_pago

class Deposito(models.Model):
  usuario = models.ForeignKey(User)
  forma_pago = models.ForeignKey(FormaPago)
  monto = models.DecimalField(max_digits=14, decimal_places=2)
  tipo_movimiento = models.ForeignKey(TipoMovimiento)
  estado = models.ForeignKey(EstadosEcommerce)

class Pago(models.Model):
  forma_pago = models.ForeignKey(FormaPago)
  cargo = models.ForeignKey(Cargo)
  monto = models.DecimalField(max_digits=14, decimal_places=2)
  deposito = models.ForeignKey(Deposito)
  tipo_movimiento = models.ForeignKey(TipoMovimiento)
  estado = models.ForeignKey(EstadosEcommerce)




#### PayPal


#========================================= MANAGERS
class CuentaPaypalManager(models.Manager):
  def obtener_cuenta_paypal(self, **kwargs):
    return self.model.objects.select_related('cat_tipoentorno', 'cat_apipaypal').get(
      cat_tipoentorno=settings.ENTORNO_PAYPAL_ID,
      habilitado=True,
      **kwargs
    )

class CuentaPayPalHabilitadosManager(models.Manager): # habilitados
    def get_query_set(self):
        return super(CuentaPayPalHabilitadosManager, self).get_query_set().filter(habilitado=True)

class CuentaPayPalEntornoManager(CuentaPayPalHabilitadosManager): # de_entorno
    def get_query_set(self):
        return super(CuentaPayPalEntornoManager, self).get_query_set().filter(cat_tipoentorno=settings.ENTORNO_PAYPAL_ID)

class CatTipoSuscripcionPayPalHabilitadosManager(models.Manager): # habilitados
    def get_query_set(self):
        return super(CatTipoSuscripcionPayPalHabilitadosManager, self).get_query_set().filter(habilitado=True)

class SubscriptionPayPalHabilitadosManager(models.Manager): # habilitados
    def get_query_set(self):
        return super(SubscriptionPayPalHabilitadosManager, self).get_query_set().filter(habilitado=True)


class CatTipoEntorno(models.Model):
  nombre = models.CharField(max_length=100)

class CatOperacionesAPIPaypal(models.Model):
  metodo = models.CharField(max_length=80, unique=True)

class CatAPIPaypal(models.Model):
  url = models.URLField()
  url_paypal = models.URLField()
  version = models.FloatField()
  cat_tipoentorno = models.ForeignKey(CatTipoEntorno)
  operaciones = models.ManyToManyField(CatOperacionesAPIPaypal, through='OpcionesAPIPaypalOperaciones')
  
  def __unicode__(self):
	return self.forma_pago

class OpcionesAPIPaypalOperaciones(models.Model):
  catapipaypal = models.ForeignKey(CatAPIPaypal)
  catoperacionesapipaypal = models.ForeignKey(CatOperacionesAPIPaypal)
  request_field = models.CharField(max_length=80)
  value = models.CharField(max_length=2048)
  habilitado = models.BooleanField(default=False)

  class Meta:
    unique_together = ('catapipaypal', 'catoperacionesapipaypal', 'request_field')

class CuentaPaypal(models.Model):
  nombre = models.CharField(max_length=100)
  apiusername = models.EmailField()
  _apipassword = models.TextField(db_column='apipassword')
  _apisignature = models.TextField(db_column='apisignature')
  cat_apipaypal = models.ForeignKey(CatAPIPaypal)

  habilitado = models.BooleanField(default=False)
  cat_tipoentorno = models.ForeignKey(CatTipoEntorno)
  receiver_email = models.EmailField(unique=True)
  #merchant_id = models.CharField(max_length=18, unique=True)
  objects = CuentaPaypalManager()
  habilitados = CuentaPayPalHabilitadosManager()
  de_entorno = CuentaPayPalEntornoManager()
  #cuenta_banco = models.ForeignKey('bancos.CuentaBanco')

  # class Meta:
  #   unique_together = ('cat_apipaypal', 'cuenta_banco')

  def get_apipassword(self):
    return base64.decodestring(self._apipassword)
  
  def set_apipassword(self, apipassword):
    self._apipassword = base64.encodestring(apipassword)
  apipassword = property(get_apipassword, set_apipassword)

  def get_apisignature(self):
    return base64.decodestring(self._apisignature)
  def set_apisignature(self, apisignature):
    self._apisignature = base64.encodestring(apisignature)
  apisignature = property(get_apisignature, set_apisignature)

class EstadosPayPal(models.Model):
  estado = models.CharField(max_length=40)

"""
class TransaccionPayPal(models.Model):
  TRANS_PENDIENTE = 1
  TRANS_PROCESADA = 2
  TRANS_FALLIDA = 6
  # PayPal IPN
  TRANS_IPN_RECIBIDO = 3
  TRANS_IPN_VERIFICADA = 4
  TRANS_IPN_INVALIDO = 5
  # Tipos de transaccion PayPal
  TRANS_SUBSCR_PAYMENT = 'subscr_payment'
  TRANS_SUBSCR_PAYMENT2 = 'subscrpayment'
  TRANS_REFERENCE_TRANSACTION = 'merchtpmt'
  TRANS_REFERENCE_TRANSACTION2 = 'merch_pmt'
  TRANS_SUBSCR_SIGNUP = 'subscr_signup'
  TRANS_NO_EXPRESS_CHECKOUT = ('send_money', TRANS_SUBSCR_PAYMENT, TRANS_SUBSCR_PAYMENT2, TRANS_REFERENCE_TRANSACTION)

  transactionid = models.CharField(max_length=19, primary_key=True)
  matricula = models.CharField(max_length=50)
  amt = models.DecimalField(max_digits=14, decimal_places=2)
  fee = models.DecimalField(max_digits=14, decimal_places=2)
  tax = models.DecimalField(max_digits=14, decimal_places=2)
  amount_received_nett = models.DecimalField(max_digits=14, decimal_places=2)
  cat_estado = models.ForeignKey(EstadosPayPal)
  cuentapaypal = models.ForeignKey(CuentaPaypal)
  fecha = models.DateTimeField(auto_now_add=True)
  orden = models.ForeignKey(OrdenCompra)
  matricula = models.CharField(max_length=100,  null=True)
  referencia_pago = models.CharField(max_length=100, null=True)
  producto_servicio = models.CharField(max_length=100, null=True)
  fee = models.DecimalField(max_digits=10, decimal_places=2)
  procesado = models.BooleanField(default=False)
  extra_info = models.TextField(null=True)
  #periodo = models.CharField(max_length=100, null=True)

  def es_procesada(self):
    return self.cat_estado_id == self.TRANS_PROCESADA

  def save(self, *args, **kwargs):
    from decimal import Decimal
    self.amount_received_nett = Decimal(self.amt) - Decimal(self.fee) - Decimal(self.tax)
    super(TransaccionPayPal, self).save(*args, **kwargs)

  def __str__(self):
    return self.transactionid

class CatTipoSuscripcionPayPal(models.Model):
  nombre = models.CharField(max_length=80)
  clave = models.CharField(max_length=30, unique=True)
  habilitado = models.BooleanField(default=True)
  objects = models.Manager()
  habilitados = CatTipoSuscripcionPayPalHabilitadosManager()

class SubscriptionPayPal(models.Model):
  subscriptionid = models.CharField(max_length=19, primary_key=True)
  matricula = models.CharField(max_length=125)
  fecha_suscripcion = models.DateTimeField()
  cuentapaypal = models.ForeignKey(CuentaPaypal)
  campus = models.CharField(max_length=100, null=True)
  nivel = models.CharField(max_length=100, null=True)
  licenciatura = models.CharField(max_length=100, null=True)
  tipo_suscripcion = models.ForeignKey(CatTipoSuscripcionPayPal)
  num_pagos = models.IntegerField(default=0)
  fecha_pp = models.DateField(null=True) # fecha primer pago
  habilitado = models.BooleanField(default=True)
  dia_cobro = models.IntegerField(null=True)
  monto = models.DecimalField(max_digits=14, decimal_places=2, default=0)
  moneda = models.ForeignKey(Moneda)
  objects = models.Manager()
  habilitados = SubscriptionPayPalHabilitadosManager()
  referencia = models.CharField(max_length=100, null=True)
  
  fecha_creacion = property(lambda self: self.fecha_suscripcion)

  # class Meta:
  #   unique_together = ('subscriptionid', 'usuario', 'licenciatura')

class SubscriptionTransaccionPayPal(models.Model):
    transactionid = models.ForeignKey(TransaccionPayPal)
    subscriptionid = models.ForeignKey(SubscriptionPayPal)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('transactionid', 'subscriptionid')


class DatosEnviadosPayPal(models.Model):
  fecha_envio = models.DateTimeField(auto_now_add=True)
  status = models.CharField(null=True, max_length=50)
  suscription = models.CharField(max_length=100)
  error = models.TextField(null=True)
"""