from django.template import Library
from biffduncandotcom.settings.prod import *
register = Library()

@register.simple_tag
def media_url():
    return MEDIA_URL