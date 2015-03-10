from netforspeech.settings.base_settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3tvox+5tih&+#1s%dn*qc8!nph+54uxci21j_4qm1(w71(v9mj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += ('debug_toolbar', )

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static asset configuration
# STATIC_ROOT isn't used

# Additional locations of static files
# STATICFILES_DIRS isn't used