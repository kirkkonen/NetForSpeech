# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0021_auto_20150407_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='communication',
        ),
        migrations.AddField(
            model_name='statement',
            name='comm_caption',
            field=models.CharField(max_length=512, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statement',
            name='comm_type',
            field=models.CharField(choices=[('PB', 'Личный ресурс'), ('ES', 'Речь на мероприятии'), ('IV', 'Интервью'), ('NS', 'Прочее')], max_length=2, default='NS'),
            preserve_default=False,
        ),
    ]
