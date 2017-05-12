from __future__ import unicode_literals
from django.db import models

from django.core.urlresolvers import reverse


class Product(models.Model):
    name = models.CharField(max_length = 100)
    upc = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=200)
    usage = models.CharField(max_length = 100)
    formula = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    amz = models.CharField(max_length=200)
