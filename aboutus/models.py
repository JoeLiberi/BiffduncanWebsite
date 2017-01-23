from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class Aboutus(CMSPlugin):
	# Services Model

	STATUS_CHOICES = (
		(1, _('Draft')),
		(2, _('Public')),
	)

	synopsis = models.TextField(_('textfield'))

	class Meta:
		verbose_name = _('aboutus')
		verbose_name_plural = _('aboutus')
		db_table  = 'aboutus'

	# cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True, default=self.Services.title)

	def __unicode__(self):
		return u'%s' % self.title