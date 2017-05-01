from django.shortcuts import render
from customer.forms import CustomerForm
# Create your views here.

def index(request):
    return render(request,'customer/index.html')

def customer(request):
    pass