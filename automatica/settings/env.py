import os
import environ
from .settings import BASE_DIR


env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env.bool("DEBUG", default=False)
SECRET_KEY = env("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}