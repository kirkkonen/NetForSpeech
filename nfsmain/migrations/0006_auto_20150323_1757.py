# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfsmain', '0005_auto_20150323_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordRelation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('relation_type', models.CharField(max_length=1, choices=[('C', 'Противоречит'), ('A', 'Соответствует')])),
            ],
        ),
        migrations.RemoveField(
            model_name='fact',
            name='facts',
        ),
        migrations.RemoveField(
            model_name='fact',
            name='statements',
        ),
        migrations.AddField(
            model_name='recordrelation',
            name='fact_1',
            field=models.ForeignKey(to='nfsmain.Fact'),
        ),
        migrations.AddField(
            model_name='recordrelation',
            name='fact_2',
            field=models.ForeignKey(related_name='facts_facts', to='nfsmain.Fact'),
        ),
        migrations.AddField(
            model_name='recordrelation',
            name='statement_1',
            field=models.ForeignKey(to='nfsmain.Statement'),
        ),
        migrations.AddField(
            model_name='recordrelation',
            name='statement_2',
            field=models.ForeignKey(related_name='statements_statements', to='nfsmain.Statement'),
        ),
        migrations.AddField(
            model_name='fact',
            name='facts1',
            field=models.ManyToManyField(through='nfsmain.RecordRelation', blank=True, to='nfsmain.Fact'),
        ),
        migrations.AddField(
            model_name='fact',
            name='statements1',
            field=models.ManyToManyField(through='nfsmain.RecordRelation', blank=True, to='nfsmain.Statement'),
        ),
        migrations.AddField(
            model_name='statement',
            name='statements1',
            field=models.ManyToManyField(through='nfsmain.RecordRelation', blank=True, to='nfsmain.Statement'),
        ),
    ]
