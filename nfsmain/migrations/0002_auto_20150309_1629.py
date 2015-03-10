# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fact',
            old_name='soruce_url',
            new_name='source_url',
        ),
    ]
