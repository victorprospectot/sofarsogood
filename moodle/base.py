


class Common(object):
	
	def __init__(self, moodleinstance):
		self.moodle = moodleinstance

	def convert_params(self, function, **values):
		params = function()
		new_params = {}
		for p in params:
			if  not values.get(p[0]) and p[2] and values.get(p[0]) != 0:
				raise Exception("El campo %s es obligatorio" % p[0])
			elif type(values.get(p[0])) != p[1] and values.get(p[0]):
				raise Exception("El campo %s debe de ser de tipo %s" % (p[0], str(p[1])))
			elif len(p) == 5 and p[4] and values.get(p[0]):
				if not(values.get(p[0]) in p[4]):
					raise Exception("El campo %s solo acepta los valores %s" % (p[0], str(p[4]) ))
				else:
					new_params[p[3]] = values.get(p[0])	
			else:
				if values.get(p[0]):
					new_params[p[3]] = values.get(p[0])
		return new_params
	