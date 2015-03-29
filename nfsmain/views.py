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


class RelationCreateViewMixIn():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ir_formset'] = self.inner_relation_formset_class(self.request.POST or None)
        context['cr_formset'] = self.cross_relation_formset_class(self.request.POST or None)
        return context

    def form_valid(self, form):
        self.object = form.save()
        ir_formset = self.inner_relation_formset_class(self.request.POST, instance=self.object)
        if ir_formset.is_valid():
            ir_formset.save()
        cr_formset = self.cross_relation_formset_class(self.request.POST, instance=self.object)
        if cr_formset.is_valid():
            cr_formset.save()
        return super().form_valid(form)


class FactCreateView(RelationCreateViewMixIn, CreateView):
    model = Fact
    fields = ['text', 'datestamp', 'timestamp', 'source_url']
    inner_relation_formset_class = FactFactFormset
    cross_relation_formset_class = FactStatementFormset


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


class StatementCreateView(RelationCreateViewMixIn, CreateView):
    model = Statement
    fields = ['speaker', 'text', 'communication', 'datestamp', 'timestamp', 'source_url', 'theme_tag']
    inner_relation_formset_class = StatementStatementFormset
    cross_relation_formset_class = StatementFactFormset


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