from django.db import models
from datetime import date
from quote.models import Quote
# Create your models here.


class Invoice(models.Model):
    date = models.DateField(default=date.today)
    to = models.CharField(max_length=50, blank=True, null=True)
    abn = models.CharField(max_length=50, blank=True, null=True)
    site = models.CharField(max_length=50, blank=True, null=True)
    quote = models.ManyToManyField(Quote)
    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    subtotal1 = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subtotal3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gst1 = models.DecimalField(max_digits=10, decimal_places=2)
    gst2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gst3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total1 = models.DecimalField(max_digits=10, decimal_places=2)
    total2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_of_dismantle = models.DateField()
    quantity1 = models.CharField(max_length=50, blank=True, null=True)
    quantity2 = models.CharField(max_length=50, blank=True, null=True)
    quantity3 = models.CharField(max_length=50, blank=True, null=True)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
