# Create your models here.
from django.db import models
from django.utils import timezone

class Portfolio(models.Model):
    date_created = models.DateTimeField('date created', default=timezone.now)
    port_name = models.CharField(max_length=100)
    port_description = models.CharField(max_length=500)

class Projects(models.Model):
    date_created = models.DateTimeField('date created', default=timezone.now)
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=500)
    project_link = models.CharField(max_length=250, blank=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)