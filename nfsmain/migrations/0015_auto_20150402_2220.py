# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0014_auto_20150329_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fact',
            name='media',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='media',
        ),
        migrations.AddField(
            model_name='fact',
            name='media_old',
            field=models.ForeignKey(to='nfsmain.Media', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='statement',
            name='media_old',
            field=models.ForeignKey(to='nfsmain.Media', null=True, blank=True),
        ),
    ]
