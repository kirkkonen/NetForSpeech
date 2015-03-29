# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0008_auto_20150323_1806'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recordrelation',
            unique_together=set([('statement_1', 'statement_2', 'fact_1', 'fact_2')]),
        ),
    ]
