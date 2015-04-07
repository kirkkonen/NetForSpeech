# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0020_auto_20150406_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='communication',
            name='caption',
            field=models.CharField(max_length=512, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='communication',
            name='type',
            field=models.CharField(choices=[('PB', 'Личный ресурс'), ('ES', 'Речь на мероприятии'), ('IV', 'Интервью'), ('NS', 'Прочее')], max_length=2, default='NS'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='factinmedia',
            name='media',
            field=models.ForeignKey(to='nfsmain.Media', blank=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='communication',
            field=models.ForeignKey(to='nfsmain.Communication'),
        ),
        migrations.AlterField(
            model_name='statementinmedia',
            name='media',
            field=models.ForeignKey(to='nfsmain.Media', blank=True),
        ),
    ]
