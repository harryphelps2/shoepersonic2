from django.db import models
from django.contrib.auth.models import User
from shop.models import Shoe

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)  
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    address_line_3 = models.CharField(max_length=100, blank=True) 
    town_or_city = models.CharField(max_length=50, blank=True)
    county = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2} {3}".format(self.id, self.date, self.full_name)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.PROTECT)
    product = models.ForeignKey(Shoe, null=False, on_delete=models.PROTECT)
    size = models.DecimalField(max_digits=5, decimal_places=1)
    quantity = models.IntegerField(blank=False)

    
    
