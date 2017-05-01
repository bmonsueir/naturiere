from django.shortcuts import render
from customer.forms import CustomerForm
# Create your views here.

def index(request):
    return render(request,'customer/index.html')

def customer(request):
    form = CustomerForm()


    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print("ERROR!")

    return render(request,'customer/customer.html',{'form':form})