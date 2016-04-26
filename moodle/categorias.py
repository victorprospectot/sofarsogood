from .base import Common

class Categorias(Common):

	def update_category(self):
		params = (
			("id", int, True, "categories[0][id]", []),
			("name", str, False, "categories[0][name]", []),
			("parent", int, False, "categories[0][parent]", []),
			("idnumber", str, False, "categories[0][idnumber]", []),
			("description", str, False, "categories[0][description]", []),
		)
		return params

	def create_category(self):
		params = (
			("name", str, True, "categories[0][name]", []),
			("parent", int, False, "categories[0][parent]", []),
			("idnumber", str, False, "categories[0][idnumber]", []),
			("description", str, False, "categories[0][description]", []),
		)
		return params

	def crear_categoria(self, **kwargs):
		function = "core_course_create_categories"
		params = self.convert_params(self.create_category, **kwargs)
		return self.moodle.make_request(function, params)

	def actualizar_categoria(self, **kwargs):
		function = "core_course_update_categories"
		params = self.convert_params(self.update_category, **kwargs)
		return self.moodle.make_request(function, params)