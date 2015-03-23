from django import forms

from nfsmain.models import *


from django.forms.models import inlineformset_factory

FactFactFormset = inlineformset_factory(Fact, FactFactRelation, exclude=[], extra=2, fk_name='fact_2')
FactStatementFormset = inlineformset_factory(Fact, FactStatementRelation, exclude=[], extra=2)