from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.utils import timezone

from django.contrib.auth.models import User
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products/products.html', {'all_products': all_products})
    
def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
  
    return render(request, 'products/product.html', {'product': product})