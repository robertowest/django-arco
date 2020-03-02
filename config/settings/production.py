from .base import *

# redefinimos la ruta de inicio
CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.abspath(os.path.join(CONFIG_DIR, '..'))

INSTALLED_APPS += [
    'apps.home',
]

DEBUG = True
ALLOWED_HOSTS = ['arcotuc.herokuapp.com']

# base de datos
import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# internalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Argentina/Tucuman'

# archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# heroku
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# archivos subidos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # python manage.py collectstatic
# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
