from django.shortcuts import render
from .models import Product
from carts.models import Cart
from django.db.models import Q 
# Create your views here.
def index(request):
    latest_product = Product.objects.all()[0:6]
    context= {
        'latest_product' : latest_product
    }
    return render(request, 'app/home.html', context)


def product_detail_page(request, pk):
    product_instance = Product.objects.get(id = pk)
    product_already_carted= False
    if request.user.is_authenticated:
        product_already_carted = Cart.objects.filter(Q(product=product_instance) & Q(user=request.user))
    context = {
        'product_instance' : product_instance,
        'product_already_carted' : product_already_carted
    }
    return render(request, 'app/productdetail.html', context)