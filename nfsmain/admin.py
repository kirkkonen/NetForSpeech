from django.contrib import admin

import nfsmain.models


class StatementStatementRelationInline(admin.StackedInline):
    model = nfsmain.models.StatementStatementRelation
    extra = 1
    fk_name = 'statement_2'


class FactFactRelationInline(admin.StackedInline):
    model = nfsmain.models.FactFactRelation
    extra = 1
    fk_name = 'fact_2'


class FactStatementRelationInline(admin.StackedInline):
    model = nfsmain.models.FactStatementRelation
    extra = 1


class FactAdmin(admin.ModelAdmin):
    inlines = (
        FactFactRelationInline,
        FactStatementRelationInline,
        )


class StatementAdmin(admin.ModelAdmin):
    inlines = (
        StatementStatementRelationInline,
        FactStatementRelationInline,
        )


# Register your models here.
admin.site.register(nfsmain.models.Organisation)
admin.site.register(nfsmain.models.Speech)
admin.site.register(nfsmain.models.Interview)
admin.site.register(nfsmain.models.Event)
admin.site.register(nfsmain.models.Fact, FactAdmin)
admin.site.register(nfsmain.models.Statement, StatementAdmin)