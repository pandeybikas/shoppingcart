from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    Full_name= models.CharField(max_length=100, null=True)
    locality= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100, choices=(
                            ('Bihar', 'Bihar'),
                            ('Delhi', 'Delhi'),
                            ('West bengal', 'West bengal'),
                            ('Punjab', 'Punjab'),
                            ('UP', 'UP'),
    ))
    zipcode= models.IntegerField()
    phone= models.IntegerField()

    def __str__(self):
        return self.name