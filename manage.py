#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # May be it is better to set a special env on Heroku
    # if 'DYNO' in os.environ:
    #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netforspeech.settings.prod_settings")
    # else:
    #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netforspeech.settings.dev_settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netforspeech.settings.dev_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
