from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from nfsmain.forms import *


def index(requst):
    template_name = "nfsmain/index.html"
    return render(requst, template_name)


class FactCreateView(CreateView):
    model = Fact
    fields = ['text', 'datestamp', 'timestamp', 'source_url']


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
    fields = ['speaker', 'text', 'communication', 'datestamp', 'timestamp', 'source_url', 'theme_tag']


class StatementListView(ListView):
    model = Statement


class StatementDetailView(DetailView):
    model = Statement