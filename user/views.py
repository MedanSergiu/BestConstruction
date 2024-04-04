from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from user.forms import UserForm
from user.models import UserModel


# Create your views here.

class CreateUserView(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('user')


class UserListView(ListView):
    model = UserModel
    template_name = 'user/all.html'

class UserDetailView(DetailView):
    model = UserModel
    template_name = 'user/detalii.html'


