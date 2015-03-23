# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0010_auto_20150323_1836'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='factfactrelation',
            unique_together=set([('fact', 'fact_2')]),
        ),
        migrations.AlterUniqueTogether(
            name='statementstatementrelation',
            unique_together=set([('statement', 'statement_2')]),
        ),
    ]
