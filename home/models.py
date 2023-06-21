from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    title= models.CharField(max_length=100)
    image= models.ImageField(upload_to='media')
    category= models.CharField(max_length=100, choices=(
                            ('Top Wear', 'Top Wear'),
                            ('Bottom Wear', 'Bottom Wear'),
                            ('Mobile', 'Mobile'),
                            ('Laptop', 'Laptop'),
                            ('Accessories', 'Accessories'),
    ))
    desc= models.TextField()
    price= models.FloatField()

    def __str__(self):
        return self.title