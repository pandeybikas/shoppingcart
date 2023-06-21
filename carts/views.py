from django.shortcuts import render, redirect
from django.http import JsonResponse
from home.models import Product
from users.models import Customer
from .models import Cart, OrderPlaced
from django.db.models import Q 
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='signin')
def add_to_cart(request):
    if request.method == 'GET':
        user= request.user
        prod_id= request.GET.get('prod_id')
        product= Product.objects.get(id=prod_id)
        Cart(user=user, product=product).save()
        return redirect('show_cart')
    
@login_required(login_url='signin')
def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    amount= 0.0
    shipping_amount = 70.0
    total_amount = 0
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]

    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
            total_amount = amount + shipping_amount
    
    context = {
        'cart_items' : cart_items,
        'amount' :amount,
        'total_amount' : total_amount
    }
    return render(request, 'app/addtocart.html',context)

@login_required(login_url='signin')
def plus_cart(request):
 if request.method == 'GET':
  prod_id=  request.GET['prod_id']
  c= Cart.objects.get(Q(product = prod_id) & Q(user= request.user))
  c.quantity+=1
  c.save()
  amount = 0.0
  shipping_amount = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
   tempamount = (p.quantity * p.product.price)
   amount += tempamount
   total_amount = amount + shipping_amount
  data = {
   'quantity' : c.quantity,
   'amount' : amount,
   'total_amount' : total_amount
  }
  return JsonResponse(data)

@login_required(login_url='signin') 
def minus_cart(request):
    if request.method == 'GET':
        prod_id=  request.GET['prod_id']
        c= Cart.objects.get(Q(product = prod_id) & Q(user= request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
            total_amount = amount + shipping_amount
        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'total_amount' : total_amount
         }
        return JsonResponse(data)

@login_required(login_url='signin')    
def remove_cart(request):
    if request.method == 'GET':
        prod_id=  request.GET['prod_id']
        c= Cart.objects.get(Q(product = prod_id) & Q(user= request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
            total_amount = amount + shipping_amount
        data = {
            
            'amount' : amount,
            'total_amount' : total_amount
         }
        return JsonResponse(data)
         

@login_required(login_url='signin')
def checkout(request):
   address_obj= Customer.objects.filter(user=request.user)
   cart_obj= Cart.objects.filter(user=request.user)
   cart_product = [p for p in Cart.objects.all() if p.user == request.user]
   amount = 0.0
   shipping_amount = 70.0
   total_amount = 0.0
   for p in cart_product:
        tempamount = (p.quantity * p.product.price)
        amount += tempamount
        total_amount = amount + shipping_amount
    
   context= {
      'address_obj' : address_obj,
      'cart_obj' : cart_obj,
      'total_amount' : total_amount
   }
   return render(request, 'app/checkout.html', context)

@login_required(login_url='signin')
def payment_done(request):
 custid= request.GET.get('custid')
 customer= Customer.objects.get(id=custid)
 cart_item = Cart.objects.filter(user=request.user)

 for c in cart_item:
  OrderPlaced(user=request.user, customer=customer, product=c.product, quantity=c.quantity, ).save()
  c.delete()
 return redirect('orders')
   
@login_required(login_url='signin')
def Orders(request):
   order_obj= OrderPlaced.objects.filter(user=request.user)
   context = {
      'order_obj' : order_obj
   }
   return render(request, 'app/orders.html', context)