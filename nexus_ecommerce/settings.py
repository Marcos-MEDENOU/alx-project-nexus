

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('NEXUS_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']




# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

