# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    replaces = [('nfsmain', '0001_initial'), ('nfsmain', '0002_auto_20150309_1629'), ('nfsmain', '0003_auto_20150309_1702'), ('nfsmain', '0004_auto_20150309_2117'), ('nfsmain', '0005_speaker'), ('nfsmain', '0006_auto_20150313_1448'), ('nfsmain', '0007_auto_20150313_1853'), ('nfsmain', '0008_remove_speaker_city')]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('soruce_url', models.CharField(max_length=2048)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(default='[ИМЯ НЕ ПРИСВОЕНО]', max_length=512)),
                ('home_url', models.CharField(max_length=512, blank=True)),
                ('state', models.CharField(default='N', choices=[('Y', 'Да'), ('N', 'Нет')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='fact',
            name='media',
            field=models.ForeignKey(to='nfsmain.Media', blank=True),
        ),
        migrations.RenameField(
            model_name='fact',
            old_name='soruce_url',
            new_name='source_url',
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('other_names', models.CharField(max_length=256, blank=True)),
                ('given_name', models.CharField(max_length=256, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='speaker',
            name='current_work',
            field=models.ForeignKey(default=None, related_name='employee_current_set', to='nfsmain.Organisation', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='previous_work',
            field=models.ManyToManyField(related_name='employee_former_set', to='nfsmain.Organisation', blank=True),
        ),
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
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
            field=models.CharField(default=None, max_length=256),
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
