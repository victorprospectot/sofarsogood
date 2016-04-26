import  socket
from httplib import HTTPSConnection, HTTPConnection, HTTPException
from sys import version_info
from urllib import urlencode

from .utils_urls import parse_url, THTTPConnection, THTTPSConnection
from django.utils.http import urlquote

class HttpRequest(object):
  def __init__(self, url, **kwargs):
    self.url = url
    self.timeout = int(kwargs.get('timeout', 5))
    self.debuglevel = int(kwargs.get('debuglevel', 0))
    self.connection = None
    self.http_config()
    self.headers = kwargs.get('headers', None)

  def http_config(self):
    self.connection_args = parse_url(self.url)
    if version_info[0] <= 2 and version_info[1] < 6:
      self.conn_class = self.connection_args[3] and THTTPSConnection or \
                                                        THTTPConnection
    else:
      self.conn_class = self.connection_args[3] and HTTPSConnection or \
                                                        HTTPConnection
    self.http_connect()

  def http_connect(self):
    """
    Setup the http connection instance.
    """
    (host, port, self.uri, is_ssl) = self.connection_args
    self.connection = self.conn_class(host, port=port, \
                                          timeout=self.timeout)
    self.connection.set_debuglevel(self.debuglevel)

  def make_request(self, method, path=[], data='', hdrs=None, parms=None):
    """
    Given a method (i.e. GET, PUT, POST, etc), data, header and
    metadata dicts, and an optional dictionary of query parameters,
    performs an http request.
    """
    path = '/%s/%s' % \
             (self.uri.rstrip('/'), '/'.join([urlquote(i) for i in path]))
    path = path.rstrip('/')

    if isinstance(parms, dict) and parms:
      path = '%s?%s' % (path, urlencode(parms))

    headers = self.headers or {}
    #headers = {'Content-Length': str(len(data)),
               #'User-Agent': self.user_agent,
               #'X-Auth-Token': self.token}
    isinstance(hdrs, dict) and headers.update(hdrs)

    def retry_request():
      '''Re-connect and re-try a failed request once'''
      self.http_connect()
      self.connection.request(method, path, data, headers)
      return self.connection.getresponse()

    try:
      self.connection.request(method, path, data, headers)
      response = self.connection.getresponse()
    except (socket.error, IOError, HTTPException):
      response = retry_request()
    #if response.status == 401:
      #self._authenticate()
      #headers['X-Auth-Token'] = self.token
      #response = retry_request()

    return response

  def close(self):
    if self.connection is not None:
      try:
        self.connection.close()
      except: pass # ignorar errores

def http_response(content, content_type="text/html", code=200, *args, **kwargs):
    from django.http import HttpResponse
    http = HttpResponse(content=content, *args, **kwargs)
    http.status_code = code
    http.content_type = content_type
    return http