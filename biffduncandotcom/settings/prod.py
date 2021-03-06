from biffduncandotcom.settings.base import *
import dj_database_url

DEBUG=False

ALLOWED_HOSTS = [
    'obscure-wildwood-69861.herokuapp.com',
    'www.biffduncan.com']

#Storage on S3 settings are stored as os.environs to keep settings.py clean
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = '{s3name}.s3.amazonaws.com'.format(s3name=AWS_STORAGE_BUCKET_NAME)
# STATIC_URL = S3_URL

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 's3utils.StaticRootS3BotoStorage'
STATIC_URL = "https://{url}/{folder}/".format(url=S3_URL, folder=STATICFILES_LOCATION)
STATIC_ROOT = "https://{url}/{folder}/".format(url=S3_URL, folder=STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_ROOT = "https://{url}/{folder}/".format(url=S3_URL, folder=MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 's3utils.MediaRootS3BotoStorage'
MEDIA_URL = "https://{url}/{folder}/".format(url=S3_URL, folder=MEDIAFILES_LOCATION)


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
    'storages',
    'boto',
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
    'tinymce'
]

urllib.parse.uses_netloc.append('postgres')
urllib.parse.uses_netloc.append('mysql')

# try:
#     db_from_env = dj_database_url.config(conn_max_age=500)
#     DATABASES['default'].update(db_from_env)
# except:
#     print ("Unexpected error:", sys.exc_info())

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


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
# EMAIL_HOST = 'smtp.biffduncan.com'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False 
# EMAIL_PORT = 25
