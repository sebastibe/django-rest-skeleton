# -*- coding: utf-8 -*-
# Django settings for api project.

import sys
import os

import dj_database_url

DEBUG = bool(os.environ.get('DEBUG', False))
TEMPLATE_DEBUG = DEBUG

TESTING = 'test' in sys.argv

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_PATH = os.path.dirname(PROJECT_ROOT)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

COMPANY = 'Acme'

VERSION = (0, 1, 0)  # (Major, Minor, Release)
VERSION_STRING = '.'.join(map(str, VERSION))

MANAGERS = ADMINS

TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/home/media/media.lawrence.com/media/'
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: 'http://media.lawrence.com/media/', 'http://example.com/media/'
MEDIA_URL = os.environ.get('MEDIA_URL', '')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/home/media/media.lawrence.com/static/'
STATIC_ROOT = os.path.join(BASE_PATH, 'static')

# URL prefix for static files.
# Example: 'http://media.lawrence.com/static/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #  'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#  Make this unique, and don't share it with anybody.
if not TESTING:
    SECRET_KEY = os.environ['SECRET_KEY']
else:
    SECRET_KEY = 'secret'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #  'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    # Uncomment the next line for CORS support
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'api.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'api.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    # external
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'south',
    'gunicorn',

    # Uncomment the next line to enable CORS with django-cors-headers
    # 'corsheaders',

    # internal
    'api.utils',
    'api.users',
)

# OAuth is optional and won't work if there is no oauth_provider & oauth2
try:
    import oauth_provider
    import oauth2
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        'oauth_provider',
    )

try:
    import provider
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        'provider',
        'provider.oauth2',
    )


if 'SENTRY_DSN' in os.environ:
    INSTALLED_APPS += (
        'raven.contrib.django',
    )

OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
)

if DEBUG:
    for app in OPTIONAL_APPS:
        if app not in INSTALLED_APPS:
            try:
                __import__(app)
            except ImportError:
                pass
            else:
                INSTALLED_APPS += (app,)

if "debug_toolbar" in INSTALLED_APPS:
    debug_mw = "debug_toolbar.middleware.DebugToolbarMiddleware"
    MIDDLEWARE_CLASSES += (debug_mw,)

AUTH_USER_MODEL = 'users.User'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# testing
# This would be if you put all your tests within a top-level 'tests' package.
TEST_DISCOVERY_ROOT = os.path.join(BASE_PATH, 'tests')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'PAGINATE_BY': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.XMLRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.XMLParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ),
}

SWAGGER_SETTINGS = {
    "exclude_namespaces": [],  # List URL namespaces to ignore
    "api_version": VERSION_STRING,  # Specify your API's version
    "enabled_methods": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    "api_key": '',  # An API key
    "is_authenticated": True,  # Set to True to enforce user authentication,
    "is_superuser": True,  # Set to True to enforce admin only access
}

PROJECT = os.environ.get('PROJECT_NAME', 'Django REST Skeleton')
HOST = os.environ.get('HOST', 'http://localhost')

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 1025)

DATABASES = {
    'default': dj_database_url.config(
        env='DATABASE_URL',
        default='postgres://username:password@localhost:5432/dbname'
    )
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_LOCATION', '127.0.0.1:6379:1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}
