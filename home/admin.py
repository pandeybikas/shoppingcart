from django.contrib import admin
from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
    list_display= ['title', 'category', 'price']

admin.site.register(Product, ProductModelAdmin)