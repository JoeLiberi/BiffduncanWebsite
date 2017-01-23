from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class ContactUs(CMSPlugin):
	# Services Model

	STATUS_CHOICES = (
		(1, _('Draft')),
		(2, _('Public')),
	)

	# Set Name
	name = models.CharField(_('name'), max_length=48)

	# Define Slug
	slug = models.SlugField(max_length=40, null = False, blank = True)

	created = models.DateTimeField(_('created'), auto_now_add=True)

	# Set Email
	email = models.EmailField(_('email'), max_length=254)

	# Message
	message = models.TextField(_('message'))

	class Meta:
		verbose_name = _('contactus')
		verbose_name_plural = _('contactus')
		db_table  = 'contactus'
		ordering  = ('-created',)
		get_latest_by = 'created'

	# cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True, default=self.Services.title)

	def __unicode__(self):
		return u'%s' % self.title

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(ContactUs, self).save(*args, **kwargs)

	def slug(sluggy):
		sluggy = sluggy.replace(' ', '-').lower()
		return slugify(sluggy)

