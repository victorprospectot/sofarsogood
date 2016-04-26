# -*- coding: utf-8 -*-
#from urllib import urlencode


from django.core.validators import URLValidator
from django.utils.http import urlencode as django_urlencode

import paypal
from .http import HttpRequest

#t = Transaccion("castillotorresvictormanuel3.h_api1.gmail.com", "SUL58F9L6VN2GE3G", "AtFwTPxiAXWxGvjVSE8yLHQ5rVRTA7NEbeZ2xcY.Ilrwh2A.22dep.4T", "https://api-3t.sandbox.paypal.com/nvp", 124)


class Transaccion(HttpRequest):
  def __init__(self, api_username, api_password, api_signature, api_url, api_version, **kwargs):
    self.api_username = api_username
    self.api_password = api_password
    self.api_signature = api_signature
    #self.api_url = api_url
    self.api_version = api_version
    super(Transaccion, self).__init__(api_url, **kwargs)
    #self.timeout = int(kwargs.get('timeout', 5))
    #self.debuglevel = int(kwargs.get('debuglevel', 0))
    #self.connection = None
    #self.http_config()

  def set_express_checkout(self, amount, return_url, cancel_url, currencyid='MXN', paymentaction=paypal.PAYPAL_SALE, **kwarg):
    # verificar si las URLs son validas
    URLValidator()(return_url) # raise ValidationError
    URLValidator()(cancel_url) # raise ValidationError

    response = self.make_request('POST', data=django_urlencode(dict(kwarg, **{
      'METHOD': paypal.PAYPAL_SET_EXPRESSCHECKOUT,
      'USER': self.api_username,
      'PWD': self.api_password,
      'SIGNATURE': self.api_signature,
      'VERSION': self.api_version,
      'PAYMENTREQUEST_0_AMT': amount,
      'PAYMENTREQUEST_0_CURRENCYCODE': currencyid,
      'RETURNURL': return_url,
      'CANCELURL': cancel_url,
      'PAYMENTREQUEST_0_PAYMENTACTION': paymentaction
    })))
    if (response.status < 200) or (response.status > 299):
      raise Exception(response.status, response.reason)
    return response

  def get_express_checkout_details(self, token):
    response = self.make_request('POST', data=django_urlencode({
      'METHOD': paypal.PAYPAL_GET_EXPRESSCHECKOUT_DETAILS,
      'USER': self.api_username,
      'PWD': self.api_password,
      'SIGNATURE': self.api_signature,
      'VERSION': self.api_version,
      'TOKEN': token
    }))
    if (response.status < 200) or (response.status > 299):
      raise Exception(response.status, response.reason)
    return response

  def do_express_checkout_payment(self, amount, token, payerid, currencyid='MXN', **kwarg):
    response = self.make_request('POST', data=django_urlencode(dict(kwarg, **{
      'METHOD': paypal.PAYPAL_DO_EXPRESSCHECKOUT_PAYMENT,
      'USER': self.api_username,
      'PWD': self.api_password,
      'SIGNATURE': self.api_signature,
      'VERSION': self.api_version,
      'TOKEN': token,
      'PAYERID': payerid,
      'PAYMENTREQUEST_0_AMT': amount,
      'PAYMENTREQUEST_0_CURRENCYCODE': currencyid,
      'PAYMENTREQUEST_0_PAYMENTACTION': paypal.PAYPAL_SALE
    })))
    if (response.status < 200) or (response.status > 299):
      raise Exception(response.status, response.reason)
    return response

  SetExpressCheckout = set_express_checkout
  GetExpressCheckoutDetails = get_express_checkout_details
  DoExpressCheckoutPayment = do_express_checkout_payment

  def validate_ipn(self, datos):
    response = self.make_request('POST', data='cmd=_notify-validate&' + datos)

    if (response.status < 200) or (response.status > 299):
      raise Exception(response.status, response.reason)
    return response

  def bm_create_button(self, buttoncode='ENCRYPTED', buttontype='SUBSCRIBE', **kwargs):
    response = self.make_request('POST', data=django_urlencode(dict(kwargs, **{
      'METHOD': 'BMCreateButton',
      'USER': self.api_username,
      'PWD': self.api_password,
      'SIGNATURE': self.api_signature,
      'VERSION': self.api_version,
      'BUTTONCODE': buttoncode,
      'BUTTONTYPE': buttontype,
    })))
    if (response.status < 200) or (response.status > 299):
      raise Exception(response.status, response.reason)
    return response

  BMCreateButton = bm_create_button

  def get_transaction_details(self, transactionid):
    response = self.make_request('POST', data=django_urlencode({
      'METHOD': 'GetTransactionDetails',
      'USER': self.api_username,
      'PWD': self.api_password,
      'SIGNATURE': self.api_signature,
      'VERSION': self.api_version,
      'TRANSACTIONID': transactionid
    }))
    if (response.status < 200) or (response.status > 299):
      raise Exception(response.status, response.reason)
    return response

  GetTransactionDetails = get_transaction_details

  def create_billing_agreement(self, token):
    response = self.make_request('POST', data=django_urlencode({
      'METHOD': 'CreateBillingAgreement',
      'USER': self.api_username,
      'PWD': self.api_password,
      'SIGNATURE': self.api_signature,
      'VERSION': self.api_version,
      'TOKEN': token
    }))
    if (response.status < 200) or (response.status > 299):
      raise Exception(response.status, response.reason)
    return response

  CreateBillingAgreement = create_billing_agreement
  
  def do_reference_transaction(self, referenceid, amt, currencyid, custom):
    import uuid
    response = self.make_request('POST', data=django_urlencode({
      'METHOD': 'DoReferenceTransaction',
      'USER': self.api_username,
      'PWD': self.api_password,
      'SIGNATURE': self.api_signature,
      'VERSION': self.api_version,
      'REFERENCEID': referenceid,
      'PAYMENTACTION': paypal.PAYPAL_SALE,
      'AMT': amt,
      'CURRENCYCODE': currencyid,
      'CUSTOM': custom,
      'MSGSUBID': uuid.uuid1()
    }))
    if (response.status < 200) or (response.status > 299):
      raise Exception(response.status, response.reason)
    return response

  DoReferenceTransaction = do_reference_transaction
