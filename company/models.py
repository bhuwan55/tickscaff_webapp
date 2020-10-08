from django.db import models
from datetime import date

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    builder_name = models.CharField(max_length=50,blank=True, null=True)
    builder_abn = models.CharField(max_length=50, blank=True, null=True)
    sub_name = models.CharField(max_length=50, default="Sam")
    sub_contact = models. BigIntegerField(default="450405743")
    quote = models.FileField(blank=True, upload_to="quotes/", null=True)


