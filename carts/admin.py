from django.contrib import admin
from .models import Cart, OrderPlaced
# Register your models here.
class CartAdminModel(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']

admin.site.register(Cart, CartAdminModel)
admin.site.register(OrderPlaced)
