from .base import *

DEBUG = False

ADMINS = (
    ('johnrumide', 'johnrumide6@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'edulearn',
        'USER': 'postgres',
        'PASSWORD': 'rumyjay10'
    }
}