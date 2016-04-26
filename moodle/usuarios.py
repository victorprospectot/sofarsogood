from .base import Common


class Alumnos(Common):
	
	def update_user_params(self):
		params = (
			("id", int, True, "users[0][id]", []),
			("username", str, False, "users[0][username]", []),
			("password", str, False, "users[0][password]", []),
			("firstname", str, False, "users[0][firstname]", []),
			("lastname", str, False, "users[0][lastname]", []),
			("email", str, False, "users[0][email]", []),
			("suspended", int, False, "users[0][suspended]", [1,0]),
			("idnumber", str, False, "users[0][idnumber]", []),
			("city", str, False, "users[0][city]", []),
			("country", str, False, "users[0][country]", []),
			("auth", str, False, "users[0][auth]", [])
		)
		return params

	def create_user_params(self):
		params = (
			("username", str, True, "users[0][username]", []),
			("password", str, False, "users[0][password]", []),
			("firstname", str, True, "users[0][firstname]", []),
			("lastname", str, True, "users[0][lastname]", []),
			("email", str, True, "users[0][email]", []),
			("suspended", int, False, "users[0][suspended]", [1,0]),
			("idnumber", str, True, "users[0][idnumber]", []),
			("auth", str, False, "users[0][idnumber]", ["db"]),
			("city", str, False, "users[0][city]", []),
			("country", str, False, "users[0][country]", [])
		)
		return params

	def enrol_user_course(self):
		
		params = (
			("roleid", int, True, "enrolments[0][roleid]", [5]),
			("userid", int, True, "enrolments[0][userid]", []),
			("courseid", int, True, "enrolments[0][courseid]", []),
			("suspend", int, False, "enrolments[0][suspend]", [1,0]),
		)

		return params

	def unenrol_user_course(self):
		
		params = (
			("roleid", int, False, "enrolments[0][roleid]", [5]),
			("userid", int, True, "enrolments[0][userid]", []),
			("courseid", int, True, "enrolments[0][courseid]", []),
		)

		return params
	
	
	def get_user_by_field(self, field, value):
		function_moodle = "core_user_get_users_by_field"
		params = {'field': field, 'values[0]': value}
		return self.moodle.make_request(function_moodle, params)

	def update_user(self, **kwargs):
		function_moodle = "core_user_update_users"
		params  = self.convert_params(self.update_user_params, **kwargs)
		return self.moodle.make_request(function_moodle, params)

	def crear_usuario(self, **kwargs):
		function_moodle = "core_user_create_users"
		params = self.convert_params(self.create_user_params, **kwargs)
		return self.moodle.make_request(function_moodle, params)

	def obtener_usuario_id(self, _id):
		return self.get_user_by_field("id", _id)

	def obtener_usuario_email(self, email):
		return self.get_user_by_field("email", email)

	def obtener_usuario_matricula(self, matricula):
		return self.get_user_by_field("idnumber", matricula)

	def suspender_usuario(self, id_user_moodle):
		return self.update_user(id=id_user_moodle, auth="nologin")

	def activar_usuario(self, id_user_moodle):
		return self.update_user(id=id_user_moodle, auth="manual")

	def matricular_usuario_curso(self, id_user_moodle, courseid, roleid=5):
		function_moodle = "enrol_manual_enrol_users"
		params = self.convert_params(self.enrol_user_course, **{'roleid': roleid, 'userid': id_user_moodle, 'courseid': courseid})
		return self.moodle.make_request(function_moodle, params)

	def desmatricular_usuario_curso(self, id_user_moodle, courseid, roleid=5):
		function_moodle = "enrol_manual_unenrol_users"
		params = self.convert_params(self.unenrol_user_course, **{'roleid': roleid, 'userid': id_user_moodle, 'courseid': courseid})
		return self.moodle.make_request(function_moodle, params)

	def suspender_usuario_curso(self, id_user_moodle, courseid, roleid=5):
		function_moodle = "enrol_manual_enrol_users"
		params = self.convert_params(self.enrol_user_course, **{'roleid': roleid, 'userid': id_user_moodle, 'courseid': courseid, 'suspend': 1})
		return self.moodle.make_request(function_moodle, params)

	def activar_usuario_curso(self, id_user_moodle, courseid, roleid=5):
		function_moodle = "enrol_manual_enrol_users"
		params = self.convert_params(self.enrol_user_course, **{'roleid': roleid, 'userid': id_user_moodle, 'courseid': courseid, 'suspend': 0})
		return self.moodle.make_request(function_moodle, params)
