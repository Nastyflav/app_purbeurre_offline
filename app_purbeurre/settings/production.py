from . import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


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

sentry_sdk.init(
    dsn="https://b902192fca2c4187bc9f286223a6bec9@o401185.ingest.sentry.io/5269916",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)