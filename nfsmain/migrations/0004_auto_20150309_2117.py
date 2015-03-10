# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0003_auto_20150309_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fact',
            name='media',
            field=models.ForeignKey(to='nfsmain.Media', blank=True),
        ),
    ]
