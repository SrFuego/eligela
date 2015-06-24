from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}

STATIC_URL = '/static/'

INTERNAL_IPS = ('127.0.0.1',)

MEDIA_ROOT = 'media/'

MEDIA_URL = '/media/'
