# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0022_auto_20150407_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='type',
            field=models.CharField(default='NS', max_length=2, choices=[('FC', 'Прогноз'), ('PR', 'Обещание'), ('OP', 'Мнение'), ('JK', 'Шутка'), ('AV', 'Совет'), ('FS', 'Факт'), ('NS', 'Другое')]),
            preserve_default=False,
        ),
    ]
