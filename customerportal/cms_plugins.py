from customerportal.models import NewEmployeePluginModel
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _


class NewEmployeePlugin(CMSPluginBase):
	model = NewEmployeePluginModel
	name = _("New Employee Form Plugin")
	render_template = "../../customerportal/templates/forms_dashboard.html"
	cache = False

	def render(self, context, insteand, placeholder):
		# context.update({'services' : ServicesPluginModel.get_all_services()})
		context = super(NewEmployeePlugin, self).render(context, instance, placeholder)
		return context

plugin_pool.register_plugin(NewEmployeePlugin)