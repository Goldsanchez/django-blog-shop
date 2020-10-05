from django.contrib import admin
from .models import CategoryProductos, Product



# Register your models here.
admin.site.register([CategoryProductos, Product])