# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0002_auto_20150316_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='comm',
            field=models.OneToOneField(primary_key=True, blank=True, serialize=False, to='nfsmain.Communication'),
        ),
        migrations.AlterField(
            model_name='speech',
            name='comm',
            field=models.OneToOneField(primary_key=True, blank=True, serialize=False, to='nfsmain.Communication'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='communication',
            field=models.CharField(max_length=256, blank=True),
        ),
    ]
