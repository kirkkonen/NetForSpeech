# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('soruce_url', models.CharField(max_length=2048)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512)),
                ('home_url', models.CharField(blank=True, max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='fact',
            name='media',
            field=models.ForeignKey(to='nfsmain.Media'),
        ),
    ]
