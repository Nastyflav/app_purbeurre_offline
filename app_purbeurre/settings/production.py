from . import *


SECRET_KEY = '#5=%f%e^58fu_9w9ynf*9=t&!0+)(gw6htzprps)fjj4!4zzuj'
DEBUG = False
ALLOWED_HOSTS = ['167.71.140.193']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'purbeurre',
        'USER': 'flavien',
        'PASSWORD': 'purpass',
        'HOST': '',
        'PORT': '5432',
    }
}