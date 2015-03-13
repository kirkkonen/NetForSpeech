from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from nfsmain.forms import *


def index(requst):
    template_name = "nfsmain/index.html"
    return render(requst, template_name)


class FactCreateView(CreateView):
    model = Fact
    fields = ['text', 'source_url']


class FactListView(ListView):
    model = Fact


class FactDetailView(DetailView):
    model = Fact


class SpeakerCreateView(CreateView):
    model = Speaker
    fields = ['index_name', 'secondary_names', 'other_names', 'birth_date', 'city', 'current_work', 'previous_work']