from __future__ import unicode_literals
from django.db import models

from django.core.urlresolvers import reverse


class Question(models.Model):
    title = models.CharField(max_length = 100)
    question = models.CharField(max_length = 255)
    answer1 = models.CharField(max_length = 100)
    answer2 = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'question', null=True, blank=True)
    count1 = models.IntegerField(default = 0)
    count2 = models.IntegerField(default = 0)