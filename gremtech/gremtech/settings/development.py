from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SECRET_KEY = 'Something secret steers at us!'

INSTALLED_APPS += [
    'debug_toolbar',
]

# Email

EMAIL_HOST = 'mail.ukraine.com.ua'
EMAIL_HOST_USER = 'webmaster@cheers-development.in.ua'
EMAIL_HOST_PASSWORD = '53o2yRjv4IKX'
