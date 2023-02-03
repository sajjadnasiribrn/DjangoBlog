from src.settings import *

SECRET_KEY = 'django-insecure-3-m=%@bh!8-06lrntmik^9pj40p3q9c&!lrvvfdr^h^^dxdp-9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# SITE
SITE_ID = 3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'