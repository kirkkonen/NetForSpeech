# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0006_auto_20150323_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fact',
            old_name='facts1',
            new_name='facts',
        ),
        migrations.RenameField(
            model_name='fact',
            old_name='statements1',
            new_name='statements',
        ),
        migrations.RenameField(
            model_name='statement',
            old_name='statements1',
            new_name='statements',
        ),
    ]
