from biffduncandotcom.settings.base import *

SECRET_KEY = 'jg84&m5n)erg)0g+l9&t&sv++#iimj70brigz(w^h-bq7g+azy'

DEBUG=True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'biffduncandotcom', 'static'),
    # os.path.join(PROJECT_ROOT, 'static'),
)
STATIC_URL = '/static/'

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


DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': DATA_DIR+ '/database.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
DEFAULT_FROM_EMAIL = 'testing@example.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False 
EMAIL_PORT = 1025
