# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0015_auto_20150402_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactInMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=2048)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatementInMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=2048)),
                ('media', models.ForeignKey(to='nfsmain.Media')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='fact',
            name='media_old',
        ),
        migrations.RemoveField(
            model_name='fact',
            name='source_url',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='media_old',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='source_url',
        ),
        migrations.AddField(
            model_name='statementinmedia',
            name='statement',
            field=models.ForeignKey(to='nfsmain.Statement'),
        ),
        migrations.AddField(
            model_name='factinmedia',
            name='fact',
            field=models.ForeignKey(to='nfsmain.Fact'),
        ),
        migrations.AddField(
            model_name='factinmedia',
            name='media',
            field=models.ForeignKey(to='nfsmain.Media'),
        ),
        migrations.AddField(
            model_name='fact',
            name='media',
            field=models.ManyToManyField(blank=True, to='nfsmain.Media', through='nfsmain.FactInMedia'),
        ),
        migrations.AddField(
            model_name='statement',
            name='media',
            field=models.ManyToManyField(blank=True, to='nfsmain.Media', through='nfsmain.StatementInMedia'),
        ),
    ]
