# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-08 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('link', models.URLField(blank='True', null='True')),
            ],
        ),
    ]
