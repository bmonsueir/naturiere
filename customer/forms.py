# from django import forms
# from customer.models import Customer

# class CustomerForm(forms.ModelForm):
#     class Meta():
#         model = Customer
#         fields = '__all__'
        


from django import forms
from django.contrib.auth.models import User

# from .project import  Project, Group




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']