from django.shortcuts import render
from django.views.generic import ListView



# Create your views here.

def home(request):
    return render(request, template_name='home/index.html', context={})


class HomeView(ListView):
    template_name = 'home/index.html'