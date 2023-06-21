from django.db import models
from home.models import Product
from django.contrib.auth.models import User
from users.models import Customer
# Create your models here.

class Cart(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username
    @property
    def product_cost(self):
        return self.quantity * self.product.price
    
class OrderPlaced(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    order_date= models.DateField(auto_now_add=True)
    status= models.CharField(max_length=100, choices=(
                    ('pending', 'pending'),
                    ('On The Way', 'On The Way'),
                    ('delivered', 'delivered'),
                    ('cancelled', 'cancelled'),
    ))

    def __str__(self):
        return self.user.username
    @property
    def tot_cost(self):
        return (self.quantity * self.product.price) + 70