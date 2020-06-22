from django.contrib import admin
from .models import Gear, Ordergear,Job, Returnedgear

# Register your models here.

admin.site.register(Gear)
admin.site.register(Ordergear)
admin.site.register(Job)
admin.site.register(Returnedgear)