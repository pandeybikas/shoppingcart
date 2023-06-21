from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    
    path('productdetail/<pk>', views.product_detail_page, name='productdetail'),
]
