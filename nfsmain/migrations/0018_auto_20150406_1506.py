# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0017_auto_20150406_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='media',
            field=models.ManyToManyField(through='nfsmain.FactInMedia', to='nfsmain.Media'),
        ),
    ]
