from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PortfolioApphook(CMSApp):
	name = _("Portfolio Apphook")

	def get_urls(self, page=None, language=None, **kwargs):
		return ["portfolio.urls"]

apphook_pool.register(PortfolioApphook)