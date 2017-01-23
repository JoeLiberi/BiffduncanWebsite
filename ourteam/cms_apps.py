from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class EmployeeApphook(CMSApp):
	name = _("Employee Apphook")

	def get_urls(self, page=None, language=None, **kwargs):
		return ["Employee.urls"]

apphook_pool.register(EmployeeApphook)