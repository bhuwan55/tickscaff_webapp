from django.db import models
from datetime import date
from company.models import Company
# Create your models here.


class Gear(models.Model):
    name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    avail_quantity = models.PositiveIntegerField()
    date = models.DateField(default=date.today)
    image = models.ImageField(null=True, upload_to="images/",blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=3)
    total_weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Ordergear(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    used_quantity = models.PositiveIntegerField()
    subtotal_weight = models.DecimalField(max_digits=10, decimal_places=2)


class Returnedgear(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    returned_quantity = models.PositiveIntegerField()
    fine_price = models.DecimalField(max_digits=10, decimal_places=3)
    remain_quantity = models.PositiveIntegerField()



STATUS_CHOICES = (
    ('active', 'active'),
    ('finished', 'finished'),
)


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="active")
    order = models.ManyToManyField(Ordergear)
    returned = models.ManyToManyField(Returnedgear)
    total_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_quantity = models.PositiveIntegerField(default=0)
    total_remain_quantity = models.PositiveIntegerField(default=0)
    site = models.CharField(max_length=100)
    date_for_installation = models.DateField(default=date.today)
    amount_of_bays = models.PositiveIntegerField(default="0")
    job_type = models.CharField(max_length=50, default="o")



