from dj_database_url import parse

from .base import *  # noqa


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

DATABASES = {
    'default': parse(config('DATABASE_URL')),
}
