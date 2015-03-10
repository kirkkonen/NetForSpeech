"""
WSGI config for netforspeech project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# May be it is better to set a special env on Heroku
if 'DYNO' in os.environ:
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netforspeech.settings.prod_settings")
    from dj_static import Cling
    application = Cling(get_wsgi_application())
else:
    application = get_wsgi_application()