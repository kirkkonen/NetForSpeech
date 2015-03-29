from django import forms

from nfsmain.models import *


from django.forms.models import inlineformset_factory

FactFactFormset = inlineformset_factory(Fact, FactFactRelation, exclude=[], extra=2, fk_name='fact_2')
FactStatementFormset = inlineformset_factory(Fact, FactStatementRelation, exclude=[], extra=2)
StatementStatementFormset = inlineformset_factory(Statement, StatementStatementRelation, exclude=[], extra=2,
                                                  fk_name='statement_2')
StatementFactFormset = inlineformset_factory(Statement, FactStatementRelation, exclude=[], extra=2)