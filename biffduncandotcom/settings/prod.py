from biffduncandotcom.settings.base import *

DEBUG=False

#Storage on S3 settings are stored as os.environs to keep settings.py clean
AWS_STORAGE_BUCKET_NAME = 'biffduncan-website'
AWS_ACCESS_KEY = 'AKIAJOPZJ2Z4NNFE6JNA'
AWS_SECRET_ACCESS_KEY = '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'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://{s3name}.s3.amazonaws.com/'.format(s3name=AWS_STORAGE_BUCKET_NAME)
STATIC_URL = S3_URL

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    # 'filer',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_link',
    # 'cmsplugin_filer_file',
    # 'cmsplugin_filer_folder',
    # 'cmsplugin_filer_image',
    # 'cmsplugin_filer_utils',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    # 'djangocms_video',
    'biffduncandotcom',
    'services.apps.ServicesConfig',
    'portfolio.apps.PortfolioConfig',
    'aboutus.apps.AboutusConfig',
    'ourteam.apps.OurteamConfig',
    'contactus.apps.ContactusConfig',
    'widget_tweaks',
    'storages',
    'boto'
    # 'django_smartfields',
]

urllib.parse.uses_netloc.append('postgres')
urllib.parse.uses_netloc.append('mysql')

try:

    if 'DATABASE_URL' in os.environ:
        url = urlparse(os.environ['DATABASE_URL'])
        DATABASES['default'] = {
            'NAME':     url.path[1:],
            'USER':     url.username,
            'PASSWORD': url.password,
            'HOST':     url.hostname,
            'PORT':     url.port,
        }
        if url.scheme == 'postgres':
            DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except:
    print ("Unexpected error:", sys.exc_info())


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
DEFAULT_FROM_EMAIL = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False 
EMAIL_PORT = 1025
