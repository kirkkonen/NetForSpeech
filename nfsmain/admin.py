from django.contrib import admin

import nfsmain.models


class StatementStatementRelationInline(admin.TabularInline):
    model = nfsmain.models.StatementStatementRelation
    extra = 1
    fk_name = 'statement_2'
#     exclude = ['fact_1', 'fact_2']


class FactFactRelationInline(admin.TabularInline):
    model = nfsmain.models.FactFactRelation
    extra = 1
    fk_name = 'fact_2'
#     exclude = ['statement_1', 'statement_2']


class FactStatementRelationInline(admin.TabularInline):
    model = nfsmain.models.FactStatementRelation
    extra = 1
#     fk_name = 'fact_1'
#     exclude = ['statement_1', 'fact_2']
#
#     def get_queryset(self, request):
#         qs = super(FactStatementRelationInline, self).get_queryset(request)
#         return qs.exclude(statement_2=None)


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