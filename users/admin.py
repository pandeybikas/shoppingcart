from django.contrib import admin
from .models import Customer
# Register your models here.
class CustomerAdminModel(admin.ModelAdmin):
    list_display= ['Full_name', 'city', 'state', 'phone']
admin.site.register(Customer, CustomerAdminModel)