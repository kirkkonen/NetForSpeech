# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0019_auto_20150406_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factinmedia',
            name='media',
            field=models.ForeignKey(blank=True, default=9, to='nfsmain.Media'),
        ),
        migrations.AlterField(
            model_name='statementinmedia',
            name='media',
            field=models.ForeignKey(blank=True, default=9, to='nfsmain.Media'),
        ),
    ]
