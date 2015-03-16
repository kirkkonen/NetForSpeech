# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0007_auto_20150313_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='city',
        ),
    ]
