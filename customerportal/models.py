from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
from django.template.defaultfilters import slugify
from django.db import models
from django.forms import ModelForm



class NewEmployee(models.Model):

	class Meta:
		verbose_name = _("NewEmployee")
		db_table  = 'NewEmployee'
		ordering  = ('-created',)
		get_latest_by = 'created'


	name = models.CharField(_('name'), max_length=48, unique=True, blank=False)
	location = models.CharField(_('location'), max_length=48, blank=False)


	slug = models.SlugField(max_length=40, null = False, blank = True)

	created = models.DateTimeField(_('created'), auto_now_add=True, primary_key=True)

	def __unicode__(self):
		return u'%s' % self.title

	def __str__(self):
		return self.name

	# def save(self, *args, **kwargs):
	# 	self.slug = slugify(self.name)
	# 	super(NewEmployee, self).save(*args, **kwargs)

	def slug(sluggy):
		sluggy = sluggy.replace(' ', '-').lower()
		return slugify(sluggy)


# class NewEmployeePluginModel(CMSPlugin):
# 	name = models.CharField(_('name'), max_length=48, unique=True, blank=False)
# 	location = models.CharField(_('location'), max_length=48, unique=True, blank=False)