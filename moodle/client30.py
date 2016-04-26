

#Token 6724cd92b3b5ddeff1f5baf680963645

class MoodleAPI(object):

	def __init__(self, token, url, format="json"):
		self.token = token
		self.format = format
		self.url = url	


	def make_request(self, function, params={}):
		import requests
		url = self.url + "?wstoken=%s&wsfunction=%s&moodlewsrestformat=%s" % (self.token, function, self.format)
		respuesta = requests.post(url, params)
		if self.format == "json":
			return respuesta.json()
		return respuesta.text


#m = MoodleAPI("6724cd92b3b5ddeff1f5baf680963645", "http://localhost/moodle/webservice/rest/server.php")
#m.make_request("core_user_get_users_by_id", {"userids[0]":2})