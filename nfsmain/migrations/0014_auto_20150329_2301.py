# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0013_auto_20150329_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='links',
        ),
        migrations.AddField(
            model_name='personallink',
            name='speaker',
            field=models.ForeignKey(default=None, to='nfsmain.Speaker'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='speaker',
            name='current_work',
            field=models.ForeignKey(blank=True, to='nfsmain.Organisation', related_name='employee_current_set', null=True),
        ),
    ]
