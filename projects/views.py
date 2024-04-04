from django.shortcuts import render, resolve_url
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from projects.forms import ProjectsForm
from projects.models import ProjectsModel


# Create your views here.

class ProjectsDetailsView(DetailView):
    template_name ="layout/base.html"
    model = ProjectsModel

class ProjectsListView(ListView):
    template_name ="layout/base.html"
    model = ProjectsModel

class ProjectsCreateView(CreateView):
    form_class = ProjectsForm
    template_name = 'create_update_form.html'
    model = ProjectsModel
    success_url = reverse_lazy('project-all')
