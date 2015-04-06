# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0018_auto_20150406_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factinmedia',
            name='media',
            field=models.ForeignKey(to='nfsmain.Media', blank=True),
        ),
        migrations.AlterField(
            model_name='statementinmedia',
            name='media',
            field=models.ForeignKey(to='nfsmain.Media', blank=True),
        ),
    ]
