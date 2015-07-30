"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# importing secrets
import json
from django.core.exceptions import ImproperlyConfigured
try:
    with open(os.path.join(os.path.dirname(__file__), "secrets.json")) as f:
        secrets = json.loads(f.read())
except IOError:
    raise ImproperlyConfigured("Unable to open secrets file. Make sure you ahve a file called secrets.json in the settings folder.")


def get_secret(setting, default=None, required=True, secrets=secrets):
    """  Get secrets from secrets.json file   """
    try:
        return secrets[setting]
    except KeyError:
        if default:
            return default
        if not required:
            return None
        error_msg = "Set the {0} variable in secrets.json".format(setting)


SECRET_KEY = get_secret('SECRET_KEY')
# why is this?

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['46.101.237.155', 'www.gaardlauget-christianshavn.dk', 'gaardlauget-christianshavn.dk']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'guestbook',
    'uploader',
    'board',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': get_secret('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC FILES
#STATIC_PATH = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/gaardlaug/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
	)


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Email settings PRODUCTION
SERVER_EMAIL = 'niels@nscp.dk'
DEFAULT_FROM_EMAIL = 'niels@nscp.dk'
ADMINS = ((u'me', 'niels@nscp.dk'),)
MANAGERS = ADMINS

# IMPORT local_settings
try:
    from .local_settings import *
except ImportError:
    pass
