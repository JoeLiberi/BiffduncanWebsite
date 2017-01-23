from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ServicesApphook(CMSApp):
	name = _("Services Apphook")

	def get_urls(self, page=None, language=None, **kwargs):
		return ["services.urls"]

apphook_pool.register(ServicesApphook)