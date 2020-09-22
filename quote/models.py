from django.db import models
from datetime import date
from main.models import Job
# Create your models here.


class Quote(models.Model):
    date = models.DateField(default=date.today)
    job = models.OneToOneField(Job, on_delete = models.CASCADE)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    hire_period = models.SmallIntegerField()
    new_scope = models.CharField(max_length=50)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    scope_end = models.TextField(blank=True, null=True)