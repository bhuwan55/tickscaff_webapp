from django.db import models
from datetime import date
from main.models import Job


# Create your models here.


class Company(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    builder_name = models.CharField(max_length=50)
    builder_abn = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=50)
    sub_contact = models. BigIntegerField()
    amount_of_bays = models.PositiveIntegerField()
    job_type = models.CharField(max_length=50)
    quote = models.FileField(blank=True, upload_to="quotes/", null=True)


