from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.template.defaultfilters import slugify


class Services(CMSPlugin):
	# Services Model

	# Set Title
	title = models.CharField(_('title'), max_length=64)
	# cmsplugin_ptr = models.CharField(_('cmsplugin_ptr_id'), max_length=24)

	# Define Slug
	slug = models.SlugField(max_length=40, null = False, blank = True)

	# Set Image upload path and image properties
	image_upload_path = 'services/%Y/%m/%d'
	image = models.ImageField(upload_to=image_upload_path, max_length=100)

	# Set the description
	description = models.CharField(_('description'), max_length=200)
	created = models.DateTimeField(_('created'), auto_now_add=True)

	class Meta:
		verbose_name = _('service')
		verbose_name_plural = _('services')
		db_table  = 'services_rendered'
		ordering  = ('-created',)
		get_latest_by = 'created'

	# cmsplugin_ptr = models.OneToOneField(CMSPlugin, related_name='+', parent_link=True, default=self.Services.title)

	def __unicode__(self):
		return u'%s' % self.title

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Services, self).save(*args, **kwargs)

	def slug(sluggy):
		sluggy = sluggy.replace(' ', '-').lower()
		return slugify(sluggy)

	def get_all_services():
		'''
		Split the services section up so its formated nicely.

		Returns a nested list with no more than 3 entries in each child list.

		Example: [[1, 2, 3], [4, 5, 6], [7, 8]]
		'''
		all_entries = Services.objects.all().order_by('created')
		tmp_l = []

		for service in all_entries:
			i = all_entries.index(service)

			if i%3 == 0:
				b_name = "b{number}".format(number=i)
				b_name = []

			if i%3 <= 2:
				b_name.append(service)

			if i%3 == 2:
				tmp_l.append(b_name)

		p = len(all_entries)%3
		tmp_l.append(all_entries[-p:])

		all_entries = tmp_l

		return all_entries
