from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from survey.models import Question

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length = 128,unique=True)
    email = models.EmailField(max_length=254,unique=True)
    survey = models.ManyToManyField(Question)
    
    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("customer:customer",kwargs={'pk':self.pk})

class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    link = models.URLField(max_length=200, null = 'True', blank = 'True')
    
    def __str__(self):
        return self.title
        
class Exposition(models.Model):
    question = models.ForeignKey(Question)
    respondent = models.ForeignKey(Customer)
    text = models.TextField()
    