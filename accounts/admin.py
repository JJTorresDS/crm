from django.contrib import admin

# Register your models here.
from .models import Customer, Product, Order, Tag

admin.site.register([Customer, Product, Order, Tag])