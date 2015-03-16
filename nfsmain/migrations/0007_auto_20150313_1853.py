# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0006_auto_20150313_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('source_url', models.CharField(max_length=2048)),
                ('datestamp', models.DateField()),
                ('timestamp', models.TimeField(null=True, blank=True)),
                ('happening', models.CharField(max_length=256, blank=True)),
                ('media', models.ForeignKey(to='nfsmain.Media', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThemeTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('caption', models.CharField(max_length=128)),
            ],
        ),
        migrations.RenameField(
            model_name='speaker',
            old_name='name',
            new_name='index_name',
        ),
        migrations.RemoveField(
            model_name='speaker',
            name='given_name',
        ),
        migrations.AddField(
            model_name='fact',
            name='datestamp',
            field=models.DateField(default=datetime.datetime(2015, 3, 13, 15, 53, 17, 261092, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='secondary_names',
            field=models.CharField(max_length=256, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fact',
            name='timestamp',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='statement',
            name='speaker',
            field=models.ForeignKey(to='nfsmain.Speaker'),
        ),
        migrations.AddField(
            model_name='statement',
            name='theme_tag',
            field=models.ManyToManyField(to='nfsmain.ThemeTag', blank=True),
        ),
    ]
