from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from nfsmain.forms import *


def index(request):
    template_name = "nfsmain/index.html"
    return render(request, template_name)


@login_required()
def admin(request):
    template_name = "nfsmain/admin.html"
    return render(request, template_name)


class InlineFormsetCreateViewMixIn():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formsets = kwargs.get('formsets')
        if not formsets:
            formsets = {formset_class: self.inlines[formset_class]() for formset_class in self.inlines}
        context.update(formsets)
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        formsets = {formset_class: self.inlines[formset_class](self.request.POST) for formset_class in self.inlines}
        if form.is_valid() and all(formset.is_valid() for formset in formsets.values()):
            return self.form_valid(form, formsets)
        else:
            return self.form_invalid(form, formsets)

    def form_valid(self, form, formsets):
        self.object = form.save()
        for formset in formsets.values():
            formset.instance = self.object
            formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formsets):
        return self.render_to_response(self.get_context_data(form=form, formsets=formsets))


class FactCreateView(InlineFormsetCreateViewMixIn, CreateView):
    model = Fact
    fields = ['text', 'datestamp', 'timestamp']
    inlines = {'fact_fact_formset': FactFactFormset, 'fact_statement_formset': FactStatementFormset,
               'fact_in_media_formset': FactInMediaFormset}


class FactListView(ListView):
    model = Fact


class FactDetailView(DetailView):
    model = Fact


class SpeakerCreateView(InlineFormsetCreateViewMixIn, CreateView):
    model = Speaker
    fields = ['index_name', 'secondary_names', 'other_names', 'birth_date', 'current_work', 'previous_work']
    inlines = {'personal_link_formset': PersonalLinkFormset}


class SpeakerListView(ListView):
    model = Speaker


class SpeakerDetailView(DetailView):
    model = Speaker


class StatementCreateView(InlineFormsetCreateViewMixIn, CreateView):
    model = Statement
    fields = ['speaker', 'text', 'type', 'comm_type', 'comm_caption', 'datestamp', 'timestamp', 'theme_tag']
    inlines = {'statement_statement_formset': StatementStatementFormset, 'statement_fact_formset': StatementFactFormset,
               'statement_in_media_formset': StatementInMediaFormset}


class StatementListView(ListView):
    model = Statement


class StatementDetailView(DetailView):
    model = Statement


class OrganisationCreateView(CreateView):
    model = Organisation
    fields = ['name']


class OrganisationListView(ListView):
    model = Organisation


class OrganisationDetailView(DetailView):
    model = Organisation