from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eligela',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.child('static')]

INTERNAL_IPS = ('127.0.0.1',)
