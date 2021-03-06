import os, sys
import urllib.parse
from urllib.parse import urlparse

gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.dirname(BASE_DIR)

SECRET_KEY = 'jg84&m5n)erg)0g+l9&t&sv++#iimj70brigz(w^h-bq7g+azy'

# MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
ROOT_URLCONF = 'biffduncandotcom.urls'
STATIC_ROOT = 'staticfiles'
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

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
    'cms.middleware.language.LanguageCookieMiddleware',
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

# CMS_TEMPLATES_DIR = {
#     1: 'biffduncandotcom/templates'
# }


CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {}

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)


RECAPTCHA_PUBLIC_KEY = '6LdYrxwUAAAAAJE4NaNTWQZKMFmWBy-y6weZ9_Vc'
RECAPTCHA_PRIVATE_KEY = '6LdYrxwUAAAAAN7KJxwGGNoR_ML_nAmjLdb4VImW'