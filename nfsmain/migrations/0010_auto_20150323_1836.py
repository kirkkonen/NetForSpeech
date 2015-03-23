# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import nfsmain.models


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0009_auto_20150323_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactFactRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
            bases=(models.Model, ),
        ),
        migrations.CreateModel(
            name='FactStatementRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
            bases=(models.Model, ),
        ),
        migrations.CreateModel(
            name='StatementStatementRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
            bases=(models.Model, ),
        ),
        migrations.AlterUniqueTogether(
            name='recordrelation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='recordrelation',
            name='fact_1',
        ),
        migrations.RemoveField(
            model_name='recordrelation',
            name='fact_2',
        ),
        migrations.RemoveField(
            model_name='recordrelation',
            name='statement_1',
        ),
        migrations.RemoveField(
            model_name='recordrelation',
            name='statement_2',
        ),
        migrations.AlterField(
            model_name='fact',
            name='facts',
            field=models.ManyToManyField(blank=True, through='nfsmain.FactFactRelation', to='nfsmain.Fact'),
        ),
        migrations.AlterField(
            model_name='fact',
            name='statements',
            field=models.ManyToManyField(blank=True, through='nfsmain.FactStatementRelation', to='nfsmain.Statement'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='statements',
            field=models.ManyToManyField(blank=True, through='nfsmain.StatementStatementRelation', to='nfsmain.Statement'),
        ),
        migrations.DeleteModel(
            name='RecordRelation',
        ),
        migrations.AddField(
            model_name='statementstatementrelation',
            name='statement',
            field=models.ForeignKey(related_name='statements_fst_set', to='nfsmain.Statement'),
        ),
        migrations.AddField(
            model_name='statementstatementrelation',
            name='statement_2',
            field=models.ForeignKey(related_name='statements_snd_set', to='nfsmain.Statement'),
        ),
        migrations.AddField(
            model_name='factstatementrelation',
            name='fact',
            field=models.ForeignKey(to='nfsmain.Fact'),
        ),
        migrations.AddField(
            model_name='factstatementrelation',
            name='statement',
            field=models.ForeignKey(to='nfsmain.Statement'),
        ),
        migrations.AddField(
            model_name='factfactrelation',
            name='fact',
            field=models.ForeignKey(related_name='facts_fst_set', to='nfsmain.Fact'),
        ),
        migrations.AddField(
            model_name='factfactrelation',
            name='fact_2',
            field=models.ForeignKey(related_name='facts_snd_set', to='nfsmain.Fact'),
        ),
        migrations.AlterUniqueTogether(
            name='factstatementrelation',
            unique_together=set([('statement', 'fact')]),
        ),
    ]
