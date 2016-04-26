"""def realizar_transaccion_paypal(cuenta_paypal, operacion, *args, **kwargs):
  from General.utils import desencripta_rsa

  ops_log = kwargs.pop('ops_log', {})
  log_transaccion_paypal(operacion, tipo_mensaje=MSJ_REQUEST, **ops_log) # bitacora de transaccion
  transaccion_paypal = Transaccion(cuenta_paypal.apiusername, desencripta_rsa(cuenta_paypal.apipassword), desencripta_rsa(cuenta_paypal.apisignature), cuenta_paypal.cat_apipaypal.url, cuenta_paypal.cat_apipaypal.version)
  respuesta_paypal = getattr(transaccion_paypal, operacion)(*args,
    **dict(cuenta_paypal.cat_apipaypal.opcionesapipaypaloperaciones_set.filter(catoperacionesapipaypal__metodo=operacion, habilitado=True).values_list('request_field', 'value'), **kwargs)
  )
  respuesta_paypal_dict = respuesta_paypal_a_dict(respuesta_paypal)
  transaccion_paypal.close() # cerrar transaccion PayPal

  ops_log.update(respuesta_paypal_dict)
  log_transaccion_paypal(operacion, tipo_mensaje=MSJ_RESPONSE, **ops_log) # bitacora de transaccion
  if respuesta_paypal_dict['ack'] == 'Success':
    return respuesta_paypal_dict
  raise TransaccionPayPalException(respuesta_paypal_dict)
  
  
  
  respuesta_paypal_dict = realizar_transaccion_paypal(
		cuenta_paypal,
		PAYPAL_SET_EXPRESSCHECKOUT,
		monto,
		url_regreso,
		url_regreso + '?accion=cancelado',
		PAYMENTREQUEST_0_DESC=descripcion,
		PAYMENTREQUEST_0_CUSTOM=matricula + "|" + programa + "|" + campus + "|" + nivel + "|" + referencia_pago + "|" + extra_info,
		currencyid=moneda, #DEBE SER cuenta_paypal.moneda,
		ops_log={
			'c_monto_enviado': float(monto),
			'c_usuario_matricula': matricula,
			'c_programa_id': programa,
			'c_campus_id': campus,
			'c_nivel_id': nivel,
			'c_cuenta_pp_id': cuenta_paypal.pk,
			'c_paymentaction': PAYPAL_SALE,
			'c_currencyid': moneda, #DEBE SER cuenta_paypal.moneda,
			'c_referencia_pago': referencia_pago,
      'c_extra': extra_info, 
      'c_periodo': periodo
		}
  return 1
"""
PAYPAL_SALE = 'Sale'
PAYPAL_AUTHORIZATION = 'Authorization'
PAYPAL_SET_EXPRESSCHECKOUT = 'SetExpressCheckout'
PAYPAL_GET_EXPRESSCHECKOUT_DETAILS = 'GetExpressCheckoutDetails'
PAYPAL_DO_EXPRESSCHECKOUT_PAYMENT = 'DoExpressCheckoutPayment'
PAYPAL_BM_CREATE_BUTTON = 'BMCreateButton'
PAYPAL_GET_TRANSACTION_DETAILS = 'GetTransactionDetails'
PAYPAL_CREATE_BILLING_AGREEMENT = 'CreateBillingAgreement'
PAYPAL_DO_REFERENCE_TRANSACTION = 'DoReferenceTransaction'



def fechahorapp_a_fechahoralocal(fechahora):
    import datetime
    import re

    if isinstance(fechahora, basestring):
        try:
            match = re.match(r'^.+(PST|PDT)$', fechahora)
            if match and match.group(1) in ('PST', 'PDT'):
                from pytz import timezone
                from dateutil import tz

                datetimepp = datetime.datetime.strptime(fechahora, '%X %b %d, %Y ' + match.group(1))
                datetimepp = timezone('US/Pacific').localize(datetimepp)
                datetimepp = datetimepp.astimezone(tz.tzlocal())
                return datetimepp.replace(tzinfo=None)
        except Exception, e:
            pass

    # en caso de no poder obtener la fecha/hora
    # PayPal a fecha/hora local, regresar la fecha/hora actual
    return datetime.datetime.now()


def respuesta_paypal_a_dict(respuesta):
  import urllib2
  new_dict = dict()
  unquoted = urllib2.unquote(respuesta).split('&')
  for item in unquoted:
    splitted = item.split('=')
    new_dict[splitted[0]] = splitted[1]
  return new_dict


