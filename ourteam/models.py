from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.template.defaultfilters import slugify


class Employee(CMSPlugin):
	# Services Model

	STATUS_CHOICES = (
		(1, _('Draft')),
		(2, _('Public')),
	)

	# Set Name
	name = models.CharField(_('name'), max_length=48)

	# Define Slug
	slug = models.SlugField(max_length=40, null = False, blank = True)

	# Set Title
	title = models.CharField(_('title'), max_length=48)

	# Set Image upload path and image properties
	image_upload_path = 'ourteam/%Y/%m/%d'
	# image = models.ImageField(upload_to=image_upload_path, max_length=100, blank=True, default='ourteam/default.jpg')

	image = fields.ImageField(upload_to=image_upload_path, 
		blank=True, default='ourteam/default.jpg', 
		dependencies=[
	        FileDependency(processor=ImageProcessor(
	            format='JPEG', scale={'max_width': 150, 'max_height': 150}))
	    ])

	created = models.DateTimeField(_('created'), auto_now_add=True)
	email = models.EmailField(_('email'), max_length=254)

	# Social Media
	twitter = models.CharField(_('twitter'), max_length=24, blank=True, default='https://www.twitter.com')
	linkedin = models.CharField(_('linkedin'), max_length=24,blank=True, default='https://www.linkedin.com')
	facebook = models.CharField(_('facebook'), max_length=24,blank=True, default='https://www.facebook.com')

	class Meta:
		verbose_name = _('employee')
		verbose_name_plural = _('employee')
		db_table  = 'employee'
		ordering  = ('-created',)
		get_latest_by = 'created'

	def __unicode__(self):
		return u'%s' % self.title

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Employee, self).save(*args, **kwargs)

	def get_all_services():
		# all_entries = Services.objects.all()
		all_entries = Employee.objects.all().order_by('created')
		return all_entries

	def slug(sluggy):
		sluggy = sluggy.replace(' ', '-').lower()
		return slugify(sluggy)
