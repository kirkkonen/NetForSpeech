from netforspeech.settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# TODO Test without it
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3tvox+5tih&+#1s%dn*qc8!nph+54uxci21j_4qm1(w71(v9mj'
# TODO Get SECRET_KEY from env variable

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Allow all host headers
ALLOWED_HOSTS = ['*']
# TODO Change to host-specific:
# ALLOWED_HOSTS = ['netforspeech.herokuapp.com']

# INSTALLED_APPS are listed in the base settings

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# TODO Enable with HTTPS:
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

# Heroku-recommended settings
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# TODO See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/ for production optimisations