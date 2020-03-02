"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os


# /project
#     /apps
#     /config
#         /settings
#             base.py
#     /static
# 
# FILE = os.path.abspath(__file__)                         == /project/config/settings/base.py
# os.path.dirname(FILE)                                    == /project/config/settings
# os.path.dirname(os.path.dirname(FILE))                   == /project/config
# os.path.dirname(os.path.dirname(os.path.dirname(FILE)))  == /project


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lf8b4b9xrm7f@x7jz46zlzl+wslamziy_!rc%-+hd#%_rbq0d1'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # aplicaciones de terceros para DESA y PROD
    'ckeditor',
    # aplicaciones propias para para DESA y PROD
    'apps.home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# barra de herramientas de CKEditor
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format'],
            {'name': 'styleBar',
             'items': ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat']},
            {'name': 'paragraphBar',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent']},
            {'name': 'justifyBar',
             'items': ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            '/',  # crea una nueva línea
            {'name': 'colorBar', 'items': ['TextColor', 'BGColor']},
            {'name': 'insertBar',
             'items': ['Image', 'HorizontalRule', 'Smiley', 'SpecialChar']},
            ['Link', 'Unlink'],
            {'name': 'toolBar', 'items': ['Maximize', 'ShowBlocks', 'Source']},
        ],
        'height': 291,
        'width': '100%',
        'tabSpaces': 4,
    }
}