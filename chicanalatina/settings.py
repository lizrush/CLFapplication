"""
Django settings for gaytabase project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from urlparse import urlparse
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j!h0x=i!_)_d52pwbrzhou+6e&c4r4^7+7zayqc(0=kzo#%cp+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'clfapplication',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'chicanalatina.urls'

WSGI_APPLICATION = 'chicanalatina.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if environ.has_key('DATABASE_URL'):
    url = urlparse(environ['DATABASE_URL'])
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '' # This is where you want the collectstatic app to put all of the files for deployment, when it pulls from multiple DIRS
STATIC_URL = '/static/' #This is the part that comes before what you are using in {% static %} tags to reference files
STATIC_DIRS = '/home/aliya/gitrepos/chicanalatina/clfapplication/static/clfapplication/' #These are where the files are actually stored - this is really important for deployment on servers like Bluehost where you can't save inside your project directory


TEMPLATE_DIRS = (
	'/home/aliya/gitrepos/chicanalatina/clfapplication/templates/clfapplication/',
	'clfapplication/templates/clfapplication/',
)

LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = 'index'

AUTH_USER_MODEL = 'auth.User'