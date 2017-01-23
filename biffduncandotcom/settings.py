import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for biffduncandotcom project.

Generated by 'django-admin startproject' using Django 1.9.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jg84&m5n)erg)0g+l9&t&sv++#iimj70brigz(w^h-bq7g+azy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition


# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
ROOT_URLCONF = 'biffduncandotcom.urls'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'biffduncandotcom', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'biffduncandotcom', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
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
    # 'django_smartfields',
)

LANGUAGES = (
    ## Customize this
    ('en-us', gettext('en-us')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en-us',
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
            'name': gettext('en-us'),
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

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

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '[::1]',
    '192.168.124.53',
    '192.168.124.65',
    '192.168.124.56',
    '192.168.124.71',
    '192.168.124.87'
    ]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
DEFAULT_FROM_EMAIL = 'testing@example.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False 
EMAIL_PORT = 1025