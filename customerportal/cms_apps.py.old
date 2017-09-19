from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class CustomerPortalApphook(CMSApp):
	name = _("CustomerPortal Apphook")

	def get_urls(self, page=None, language=None, **kwargs):
		return ["customerportal.urls"]

apphook_pool.register(CustomerPortalApphook)