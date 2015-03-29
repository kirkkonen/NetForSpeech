# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0003_auto_20150316_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='related',
            field=models.ManyToManyField(related_name='related_rel_+', blank=True, to='nfsmain.Fact'),
        ),
        migrations.AddField(
            model_name='statement',
            name='related',
            field=models.ManyToManyField(related_name='related_rel_+', blank=True, to='nfsmain.Statement'),
        ),
    ]
