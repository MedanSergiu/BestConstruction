from django.shortcuts import render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from about.forms import AboutForm
from about.models import NewsLetterModel


# Create your views here.

class AboutDetailsView(DetailView):
    template_name ="layout/base.html"
    model = NewsLetterModel

class AboutListView(ListView):
    template_name ="layout/base.html"
    model = NewsLetterModel





