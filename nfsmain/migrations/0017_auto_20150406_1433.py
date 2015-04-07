# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0016_auto_20150402_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factfactrelation',
            name='fact',
            field=models.ForeignKey(to='nfsmain.Fact', related_name='facts_base_set'),
        ),
        migrations.AlterField(
            model_name='factfactrelation',
            name='fact_2',
            field=models.ForeignKey(to='nfsmain.Fact', related_name='facts_set'),
        ),
        migrations.AlterField(
            model_name='statementstatementrelation',
            name='statement',
            field=models.ForeignKey(to='nfsmain.Statement', related_name='statements_base_set'),
        ),
        migrations.AlterField(
            model_name='statementstatementrelation',
            name='statement_2',
            field=models.ForeignKey(to='nfsmain.Statement', related_name='statements_set'),
        ),
    ]
