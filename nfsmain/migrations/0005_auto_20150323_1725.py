# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0004_auto_20150323_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fact',
            name='related',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='related',
        ),
        migrations.AddField(
            model_name='fact',
            name='facts',
            field=models.ManyToManyField(blank=True, related_name='facts_rel_+', to='nfsmain.Fact'),
        ),
        migrations.AddField(
            model_name='fact',
            name='statements',
            field=models.ManyToManyField(blank=True, to='nfsmain.Statement'),
        ),
    ]
