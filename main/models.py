from django.db import models
from datetime import date

# Create your models here.


class Gear(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    avail_quantity = models.PositiveIntegerField()
    date = models.DateField(default=date.today)
    image = models.ImageField(null=True, upload_to="images/",blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Ordergear(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.DO_NOTHING)
    used_quantity = models.PositiveIntegerField()
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2)


class Returnedgear(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.DO_NOTHING)
    returned_quantity = models.PositiveIntegerField()
    fine_price = models.DecimalField(max_digits=10, decimal_places=2)
    remain_quantity = models.PositiveIntegerField()



STATUS_CHOICES = (
    ('active', 'active'),
    ('finished', 'finished'),
)


class Job(models.Model):
    company_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default="active")
    order = models.ManyToManyField(Ordergear)
    returned = models.ManyToManyField(Returnedgear)
    date = models.DateField(default=date.today)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_quantity = models.PositiveIntegerField(default=0)
    total_remain_quantity = models.PositiveIntegerField(default=0)