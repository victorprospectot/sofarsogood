import re
from operator import itemgetter

class TransaccionPayPalException(Exception):
  def __init__(self, respuesta_paypal_dict={}, **kwargs):
    self.respuesta_paypal_dict = respuesta_paypal_dict
    self.shortmessages_re = kwargs.get('shortmessages_re', r'^L_SHORTMESSAGE(\d{1,2})$')
    self.longmessages_re = kwargs.get('longmessages_re', r'^L_LONGMESSAGE(\d{1,2})$')
    super(TransaccionPayPalException, self).__init__()

  def __str__(self):
    return '\n'.join(['%s (%s)' % msj for msj in self.errores])

  def obtener_errores_respuesta_paypal_desde_dict(self):
    obtener_mensajes = lambda _re: map(lambda t: (re.match(_re, t[0], flags=re.I).group(1), t[1]), filter(lambda t: re.match(_re, t[0], flags=re.I), self.respuesta_paypal_dict.items()))
    return map(lambda t: (t[0][1], t[1][1]), zip(sorted(obtener_mensajes(self.shortmessages_re), key=itemgetter(0)), sorted(obtener_mensajes(self.longmessages_re), key=itemgetter(0))))
  errores = property(obtener_errores_respuesta_paypal_desde_dict)