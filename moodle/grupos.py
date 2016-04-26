from .base import Common


class Grupos(Common):
	
	def create_group_params(self):
		params = (
			("courseid", int, True, "groups[0][courseid]", []),
			("name", str, True, "groups[0][name]", []),
			("description", str, True, "groups[0][description]", []),
		)
		return params

	def add_group_member_params(self):
		params = (
			("groupid", int, True, "members[0][groupid]", []),
			("userid", int, True, "members[0][userid]", []),
		)
		return params

	def delete_group_member_params(self):
		params = (
			("groupid", int, True, "members[0][groupid]", []),
			("userid", int, True, "members[0][userid]", []),
		)
		return params

	def crear_grupo(self, **kwargs):
		function_moodle = "core_group_create_groups"
		params = self.convert_params(self.create_group_params, **kwargs)
		return self.moodle.make_request(function_moodle, params)

	def agregar_persona_grupo(self, **kwargs):
		function_moodle = "core_group_add_group_members"
		params = self.convert_params(self.add_group_member_params, **kwargs)
		return self.moodle.make_request(function_moodle, params)

	def borrar_persona_grupo(self, **kwargs):
		function_moodle = "core_group_delete_group_members"
		params = self.convert_params(self.delete_group_member_params, **kwargs)
		return self.moodle.make_request(function_moodle, params)