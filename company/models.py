from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to="images/",blank=True)
