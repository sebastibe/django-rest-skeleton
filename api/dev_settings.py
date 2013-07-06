# -*- coding: utf-8 -*-
import dj_database_url

PROJECT = 'Django REST Skeleton (Dev)'
HOST = 'http://localhost'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

DATABASES = {
    'default': dj_database_url.config(
        env='DATABASE_URL',
        default='postgres://database-user:database-password@localhost:5432/database-name'
    )
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
