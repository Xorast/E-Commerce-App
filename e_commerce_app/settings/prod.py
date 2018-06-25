from .base import *

SECRET_KEY      = os.environ.get("SECRET_KEY")

DEBUG           = True

ALLOWED_HOSTS   = ["xa-django-e-commerce.herokuapp.com"]

DATABASES       = {}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL       = ''
STATICFILES_DIRS = ''
STATIC_ROOT      = ''

MEDIA_URL        = ''
MEDIA_ROOT       = ''