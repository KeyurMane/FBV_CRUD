from django.contrib import admin
from django.db import models
from .models import Laptop
# Register your models here.

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['lname','brand','price','ram']

admin.site.register(Laptop,LaptopAdmin)
