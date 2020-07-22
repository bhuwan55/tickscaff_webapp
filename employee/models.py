import datetime
from datetime import date
from django.utils.timesince import timesince
from django.db import models

# Create your models here.


class Work(models.Model):
    date = models.DateField(default=date.today)
    arrival_time = models.TimeField()
    signoff_time = models.TimeField()
    hours = models.DurationField()

    def get_time_diff(self):
        ahr = int(self.arrival_time[0:2])
        amin = int(self.arrival_time[3:5])
        shr = int(self.signoff_time[0:2])
        smin = int(self.signoff_time[3:5])

        dt1 = datetime.datetime.combine(datetime.datetime.now(), datetime.time(ahr, amin))
        dt2 = datetime.datetime.combine(datetime.datetime.now(), datetime.time(shr, smin))
        return timesince(dt1, dt2)  # Assuming dt2 is the more recent time


class Employee(models.Model):
    name = models.CharField(max_length=100)
    work = models.ManyToManyField(Work)
    total_hours = models.DurationField()
