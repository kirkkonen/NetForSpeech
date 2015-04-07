# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0020_auto_20150406_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='communication',
        ),
        migrations.AddField(
            model_name='communication',
            name='caption',
            field=models.CharField(max_length=512, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='communication',
            name='type',
            field=models.CharField(max_length=2, default='NS', choices=[('PB', 'Личный ресурс'), ('ES', 'Речь на мероприятии'), ('IV', 'Интервью'), ('NS', 'Прочее')]),
            preserve_default=False,
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
            field=models.CharField(max_length=2, default='NS', choices=[('PB', 'Личный ресурс'), ('ES', 'Речь на мероприятии'), ('IV', 'Интервью'), ('NS', 'Прочее')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statement',
            name='type',
            field=models.CharField(max_length=2, default='NS', choices=[('FC', 'Прогноз'), ('PR', 'Обещание'), ('OP', 'Мнение'), ('JK', 'Шутка'), ('AV', 'Совет'), ('FS', 'Факт'), ('NS', 'Другое')]),
            preserve_default=False,
        ),
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
