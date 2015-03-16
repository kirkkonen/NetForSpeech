# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0004_auto_20150309_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=256)),
                ('other_names', models.CharField(max_length=256, blank=True)),
                ('given_name', models.CharField(max_length=256, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
            ],
        ),
    ]
