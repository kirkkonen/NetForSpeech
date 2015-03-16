# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0004_auto_20150313_1448'),
        ('nfsmain', '0005_speaker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='speaker',
            name='city',
            field=models.ForeignKey(to='cities_light.City', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='speaker',
            name='current_work',
            field=models.ForeignKey(related_name='employee_current_set', to='nfsmain.Organisation', blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speaker',
            name='previous_work',
            field=models.ManyToManyField(related_name='employee_former_set', blank=True, to='nfsmain.Organisation'),
        ),
    ]
