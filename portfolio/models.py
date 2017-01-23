from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.template.defaultfilters import slugify

class Portfolio(CMSPlugin):
	# Services Model

	STATUS_CHOICES = (
		(1, _('Draft')),
		(2, _('Public')),
	)

	# Set Title
	title = models.CharField(_('title'), max_length=48)

	# Define Slug
	slug = models.SlugField(max_length=40, null = False, blank = True)

	# Set Image upload path and image properties
	image_upload_path = 'portfolio/%Y/%m/%d'
	image = models.ImageField(upload_to=image_upload_path, max_length=100)

	# image = fields.ImageField(upload_to=image_upload_path, 
	# 	dependencies=[
	#         FileDependency(processor=ImageProcessor(
	#             format='JPEG',))
	#     ])

	# Set the description
	# description = models.CharField(_('description'), max_length=48)
	created = models.DateTimeField(_('created'), auto_now_add=True)
	synopsis = models.TextField(_('textfield'))

	class Meta:
		verbose_name = _('portfolio')
		verbose_name_plural = _('portfolios')
		db_table  = 'portfolio'
		ordering  = ('-created',)
		get_latest_by = 'created'

	# cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True, default=self.Services.title)

	def __unicode__(self):
		return u'%s' % self.title

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Portfolio, self).save(*args, **kwargs)

	def slug(sluggy):
		sluggy = sluggy.replace(' ', '-').lower()
		return slugify(sluggy)

	def get_all_services():
		# all_entries = Services.objects.all()
		all_entries = Portfolio.objects.all().order_by('created')
		return all_entries