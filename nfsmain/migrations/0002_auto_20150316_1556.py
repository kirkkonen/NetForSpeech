# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0001_squashed_0008_remove_speaker_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.RemoveField(
            model_name='statement',
            name='happening',
        ),
        migrations.AlterField(
            model_name='fact',
            name='datestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='statement',
            name='datestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.RemoveField(
            model_name='statement',
            name='theme_tag',
        ),
        migrations.AddField(
            model_name='statement',
            name='theme_tag',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('comm', models.OneToOneField(serialize=False, to='nfsmain.Communication', primary_key=True)),
                ('origin', models.ForeignKey(to='nfsmain.Media')),
            ],
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('comm', models.OneToOneField(serialize=False, to='nfsmain.Communication', primary_key=True)),
                ('origin', models.ForeignKey(to='nfsmain.Event')),
            ],
        ),
        migrations.AddField(
            model_name='statement',
            name='communication',
            field=models.ForeignKey(default=None, to='nfsmain.Communication'),
            preserve_default=False,
        ),
    ]
