from django.db import models
from datetime import date


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    date_for_installation = models.DateField(default=date.today)
