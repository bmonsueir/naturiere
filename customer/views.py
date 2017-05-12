from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.utils import timezone
from blog.models import Post
from .models import Article
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    post = Post.objects.latest('created_date')
    all_articles = Article.objects.all()
    context = {"post":post,
                "all_articles": all_articles
    }
    return render(request,'customer/index.html', context)

def customer(request):
    return render(request, 'customer/customer.htnl')

def about(request):
    return render(request, 'customer/about.html')
    

class AboutView(TemplateView):
    template_name = 'about.html'
    
def logout_view(request):
    logout(request)
    return render(request, 'customer/logout_view.html')
    

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'customer/index.html')
          
        else:
            return render(request, 'customer/sign_up.html', {'error_message': 'Your account has been disabled'})
    else:
        return render(request, 'customer/login_view.html', {'error_message': 'Invalid login'})
            
    return render(request, 'customer/login_view.html')

def sign_up(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                
                login(request, user)
                return render(request, 'customer/index.html')
    context = {
        "form": form,
    }
    return render(request, 'customer/sign_up.html', context)
