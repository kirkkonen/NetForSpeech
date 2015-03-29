# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0007_auto_20150323_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordrelation',
            name='fact_1',
            field=models.ForeignKey(null=True, to='nfsmain.Fact'),
        ),
        migrations.AlterField(
            model_name='recordrelation',
            name='fact_2',
            field=models.ForeignKey(related_name='facts_facts', to='nfsmain.Fact', null=True),
        ),
        migrations.AlterField(
            model_name='recordrelation',
            name='statement_1',
            field=models.ForeignKey(null=True, to='nfsmain.Statement'),
        ),
        migrations.AlterField(
            model_name='recordrelation',
            name='statement_2',
            field=models.ForeignKey(related_name='statements_statements', to='nfsmain.Statement', null=True),
        ),
    ]
