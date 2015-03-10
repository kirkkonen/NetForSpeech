# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0002_auto_20150309_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='state',
            field=models.CharField(max_length=1, default='N', choices=[('Y', 'Да'), ('N', 'Нет')]),
        ),
        migrations.AlterField(
            model_name='media',
            name='name',
            field=models.CharField(max_length=512, default='[ИМЯ НЕ ПРИСВОЕНО]'),
        ),
    ]
