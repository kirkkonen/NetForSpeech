# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0011_auto_20150323_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='factfactrelation',
            name='relation_type',
            field=models.CharField(choices=[('C', 'Противоречит'), ('A', 'Соответствует')], max_length=1, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factstatementrelation',
            name='relation_type',
            field=models.CharField(choices=[('C', 'Противоречит'), ('A', 'Соответствует')], max_length=1, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statementstatementrelation',
            name='relation_type',
            field=models.CharField(choices=[('C', 'Противоречит'), ('A', 'Соответствует')], max_length=1, default=None),
            preserve_default=False,
        ),
    ]
