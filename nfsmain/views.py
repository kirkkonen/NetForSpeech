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


class FactCreateView(CreateView):
    model = Fact
    fields = ['text', 'datestamp', 'timestamp', 'source_url']

    def get_context_data(self, **kwargs):
        context = super(FactCreateView, self).get_context_data(**kwargs)
        context['fact_fact_formset'] = FactFactFormset(self.request.POST or None)
        context['fact_statement_formset'] = FactStatementFormset(self.request.POST or None)
        return context

    def form_valid(self, form):
        self.object = form.save()
        fact_fact_formset = FactFactFormset(self.request.POST, instance=self.object)
        if fact_fact_formset.is_valid():
            fact_fact_formset.save()
        fact_statement_formset = FactStatementFormset(self.request.POST, instance=self.object)
        if fact_statement_formset.is_valid():
            fact_statement_formset.save()
        return super(FactCreateView, self).form_valid(form)


class FactListView(ListView):
    model = Fact


class FactDetailView(DetailView):
    model = Fact


class SpeakerCreateView(CreateView):
    model = Speaker
    fields = ['index_name', 'secondary_names', 'other_names', 'birth_date', 'current_work', 'previous_work']


class SpeakerListView(ListView):
    model = Speaker


class SpeakerDetailView(DetailView):
    model = Speaker


class StatementCreateView(CreateView):
    model = Statement
    fields = ['speaker', 'text', 'communication', 'datestamp', 'timestamp', 'source_url', 'theme_tag', 'statements',
              'facts']


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