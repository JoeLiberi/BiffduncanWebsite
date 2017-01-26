from django.template import Library
from biffduncandotcom.settings import MEDIA_URL
register = Library()

@register.simple_tag
def media_url():
    return MEDIA_URL