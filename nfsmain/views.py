from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required

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
        for formset in self.inline_formsets:
            context[formset] = self.inline_formsets[formset](self.request.POST or None)
        return context

    def form_valid(self, form):
        self.object = form.save()
        for formset in self.inline_formsets:
            formset_object = self.inline_formsets[formset](self.request.POST, instance=self.object)
            if formset_object.is_valid():
                formset_object.save()
        return super().form_valid(form)


class FactCreateView(InlineFormsetCreateViewMixIn, CreateView):
    model = Fact
    fields = ['text', 'datestamp', 'timestamp', 'source_url']
    inline_formsets = {'fact_fact_formset': FactFactFormset, 'fact_statement_formset': FactStatementFormset}


class FactListView(ListView):
    model = Fact


class FactDetailView(DetailView):
    model = Fact


class SpeakerCreateView(InlineFormsetCreateViewMixIn, CreateView):
    model = Speaker
    fields = ['index_name', 'secondary_names', 'other_names', 'birth_date', 'current_work', 'previous_work']
    inline_formsets = {'personal_link_formset': PersonalLinkFormset}


class SpeakerListView(ListView):
    model = Speaker


class SpeakerDetailView(DetailView):
    model = Speaker


class StatementCreateView(InlineFormsetCreateViewMixIn, CreateView):
    model = Statement
    fields = ['speaker', 'text', 'communication', 'datestamp', 'timestamp', 'source_url', 'theme_tag']
    inline_formsets = {'statement_statement_formset': StatementStatementFormset,
                       'statement_fact_formset': StatementFactFormset}


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