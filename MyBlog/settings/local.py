from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SMTP Email settings

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'codingduckblog@gmail.com'
EMAIL_HOST_PASSWORD = 'MyFamily2016'
EMAIL_PORT = 587
EMAIL_USE_TLS = True