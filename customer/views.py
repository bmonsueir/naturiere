from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.utils import timezone


from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from customer.forms import CustomerForm
# Create your views here.

def index(request):
    return render(request,'customer/index.html')

def customer(request):
    return render(request, 'customer/customer.htnl')

def about(request):
    return render(request, 'customer/about.html')
    
def sign_up(request):
    return render(request, 'customer/sign_up.html')
    
def login(request):
    return render(request, 'customer/sign_up.html')
    
def logout(request):
    return render(request, 'customer/sign_up.html')
    
class AboutView(TemplateView):
    template_name = 'about.html'