from nfsmain.models import *
from nfsmain.formset_ex import RequiredInlineFormSet

from django.forms.models import inlineformset_factory

FactFactFormset = inlineformset_factory(Fact, FactFactRelation, exclude=[], extra=2, fk_name='fact_2')
FactStatementFormset = inlineformset_factory(Fact, FactStatementRelation, exclude=[], extra=2)
StatementStatementFormset = inlineformset_factory(Statement, StatementStatementRelation, exclude=[], extra=2,
                                                  fk_name='statement_2')
StatementFactFormset = inlineformset_factory(Statement, FactStatementRelation, exclude=[], extra=2)

FactInMediaFormset = inlineformset_factory(Fact, FactInMedia, fields=['source_url'], formset=RequiredInlineFormSet)
StatementInMediaFormset = inlineformset_factory(Statement, StatementInMedia, exclude=[])

PersonalLinkFormset = inlineformset_factory(Speaker, PersonalLink, exclude=[])