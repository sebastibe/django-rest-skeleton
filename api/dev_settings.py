# -*- coding: utf-8 -*-
PROJECT = 'Django REST Skeleton (Dev)'
HOST = 'http://localhost'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database-name',
        'USER': 'database-user',
        'PASSWORD': 'database-password',
        'HOST': '',
        'PORT': '',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}
