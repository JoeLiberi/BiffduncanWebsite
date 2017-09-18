from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from services.models import Services as ServicesPluginModel
from portfolio.models import Portfolio as PortfolioPluginModel
from aboutus.models import Aboutus as AboutusPluginModel
from contactus.models import ContactUs as ContactusPluginModel
from django.utils.translation import ugettext_lazy as _
from sekizai.context import SekizaiContext                                      
from customerportal.models import NewEmployeePluginModel

class ServicesPlugin(CMSPluginBase):
	model = ServicesPluginModel
	name = _("Services Plugin")
	render_template = "services.html"
	cache = False

	def render(self, context, insteand, placeholder):
		# context.update({'services' : ServicesPluginModel.get_all_services()})
		context = super(ServicesPlugin, self).render(context, instance, placeholder)
		return context

class PortfolioPlugin(CMSPluginBase):
	model = PortfolioPluginModel
	name = _("Portfolio Plugin")
	render_template = "portfolio.html"
	cache = False

	def render(self, context, insteand, placeholder):
		# context.update({'services' : ServicesPluginModel.get_all_services()})
		context = super(PortfolioPlugin, self).render(context, instance, placeholder)
		return context

class AboutusPlugin(CMSPluginBase):
	model = AboutusPluginModel
	name = _("Aboutus Plugin")
	render_template = "Aboutus.html"
	cache = False

	def render(self, context, insteand, placeholder):
		# context.update({'services' : ServicesPluginModel.get_all_services()})
		context = super(AboutusPlugin, self).render(context, instance, placeholder)
		return context

class ContactusPlugin(CMSPluginBase):
	model = ContactusPluginModel
	name = _("Contactus Plugin")
	render_template = "Contactus.html"
	cache = False

	def render(self, context, insteand, placeholder):
		# context.update({'services' : ServicesPluginModel.get_all_services()})
		context = super(ContactusPlugin, self).render(context, instance, placeholder)
		return context

plugin_pool.register_plugin(ServicesPlugin)
plugin_pool.register_plugin(ContactusPlugin)

