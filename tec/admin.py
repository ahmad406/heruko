from django.contrib import admin
from ecom.models import Product
from .models import feedback

# Register your models here.

admin.site.register(Product)
admin.site.register(feedback)
