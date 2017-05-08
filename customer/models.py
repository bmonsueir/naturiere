from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length = 128,unique=True)
    email = models.EmailField(max_length=254,unique=True)
    
    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("customer:customer",kwargs={'pk':self.pk})

