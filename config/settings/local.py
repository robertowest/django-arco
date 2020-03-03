from .base import *



# ruta del proyecto (bajamos tres niveles para llegar a la ruta del proyecto)
FILE_DIR = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(FILE_DIR)))
DEBUG = True
ALLOWED_HOSTS = ['localhost']


# aplicaciones para desarrollo
# INSTALLED_APPS += []


# base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# autenticación
AUTH_PASSWORD_VALIDATORS = []


# internalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Tucuman'


# archivos estáticos
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# archivos subidos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# python manage.py collectstatic
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')


# configuración debug-toolbar
if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker
