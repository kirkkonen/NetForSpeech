# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0012_auto_20150323_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('type', models.CharField(max_length=2, choices=[('FB', 'Facebook'), ('VK', 'Вконтакте'), ('TW', 'Twitter'), ('GB', 'Личный блог')])),
                ('uri', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='speaker',
            name='links',
            field=models.ManyToManyField(to='nfsmain.PersonalLink', blank=True),
        ),
    ]
