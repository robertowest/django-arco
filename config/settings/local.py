from .base import *

INSTALLED_APPS += [
    'apps.home',
]

DEBUG = True
ALLOWED_HOSTS = ['localhost']

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Tucuman'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', 'static'),
)

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
