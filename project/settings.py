"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# from easy_thumbnails.conf import Settings as thumbnail_settings

SITE_ID = 2

AUTH_USER_MODEL = 'authentication.Account'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7j09%e0uap(m5o=3967!k7$vp*kvg7-vr8jmslft_53g$5i@%+'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
ADMIN_EMAIL = 'hechnya@mail.ru'
ALLOWED_HOSTS = ['*']
DEBUG404 = True

# DEBUG = True
# ADMIN_EMAIL = 'hechnya@mail.ru'
# ALLOWED_HOSTS = []


YANDEX_MAPS_API_KEY="ALSB2FUBAAAAuT1HFQIA05P0YDsaQFcpdBUlKV5eo0w2lyoAAAAAAAAAAAAYL7umcMccsI8_av_IphC-iwwgdA=="


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'project.core',
    'ckeditor',
    'mptt',
    'mptt_tree_editor',
    'sitetree',
    'image_cropping',
    'easy_thumbnails',
    'project.cart',
    'authentication',
    'robokassa',
    'breadcrumbs',
    'yandex_maps',

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
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'project/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
# )

# WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_ROOT = ''

MEDIA_ROOT = '%s/project/media' % BASE_DIR

MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = '/media/uploads'

THUMBNAIL_DEBUG = True


# THUMBNAIL_PROCESSORS = (
#     'image_cropping.thumbnail_processors.crop_corners',
# ) + thumbnail_settings.THUMBNAIL_PROCESSORS


ROBOKASSA_LOGIN = 'kastoreum'
ROBOKASSA_PASSWORD1 = 'LKJHlkvbsklcbfwe2ye2893'
ROBOKASSA_PASSWORD2 = 'JJHHFHGD213Ksaf'
ROBOKASSA_TEST_MODE = True


try:
    from settings_local import *
except ImportError:
    pass

