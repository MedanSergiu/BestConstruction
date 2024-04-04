from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView, PasswordResetView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authentification.forms import CreateUserForm


# Create your views here.

class LoginUserView(LoginView):
    template_name = "login/login.html"

class UserChangePasswordView(PasswordChangeView):
    template_name = "authentification/form.html"
    success_url = reverse_lazy('user')

class CreateUserView(CreateView):
    template_name = "authentification/form.html"
    form_class =CreateUserForm
    success_url = reverse_lazy('user')

class LogoutUserView(LogoutView):
    success_url = reverse_lazy('user')

class ResetUserPassword(PasswordResetView):
    success_url = reverse_lazy('user')