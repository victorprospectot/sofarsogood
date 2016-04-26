from .base import Common

class Cursos(Common):
	

	def create_course(self):
		params = (
			("fullname", str, True, "courses[0][fullname]", []),
			("shortname", str, True, "courses[0][shortname]", []),
			("idnumber", str, False, "courses[0][idnumber]", []),
			("categoryid", int, True, "courses[0][categoryid]", []),
			("summary", str, False, "courses[0][summary]", []),
			("format", str, True, "courses[0][format]", ["weeks"]),
			("startdate", str, False, "courses[0][startdate]", []),
			("groupmode", int, False, "courses[0][groupmode]", [0, 1, 2]),#no group, separate, visible
			("groupmodeforce", int, False, "courses[0][groupmodeforce]", [0, 1]),# yes, no
			("numsections", int, True, "courses[0][numsections]", []),
		)
		return params

	def update_course(self):
		params = (
			("id", int, True, "courses[0][id]", []),
			("fullname", str, False, "courses[0][fullname]", []),
			("shortname", str, False, "courses[0][shortname]", []),
			("idnumber", str, False, "courses[0][idnumber]", []),
			("categoryid", int, False, "courses[0][categoryid]", []),
			("summary", str, False, "courses[0][summary]", []),
			("format", str, False, "courses[0][format]", ["weeks"]),
			("startdate", str, False, "courses[0][startdate]", []),
			("groupmode", int, False, "courses[0][groupmode]", [1,2]),
			("groupmodeforce", int, False, "courses[0][groupmodeforce]", [1]),
			("numsections", int, False, "courses[0][numsections]", []),
		)
		return params
	
	
	def crear_curso(self, **kwargs):
		function = "core_course_create_courses"
		params = self.convert_params(self.create_course, **kwargs)
		return self.moodle.make_request(function, params)

	def actualizar_curso(self, **kwargs):
		function = "core_course_update_courses"
		params = self.convert_params(self.update_course, **kwargs)
		return self.moodle.make_request(function, params)