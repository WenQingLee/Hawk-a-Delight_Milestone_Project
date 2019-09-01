from django.db import models
from restaurant_app.models import MenuItem

# Create your models here.

class Order(models.Model):
    full_name = models.CharField(max_length=200, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.fullname)
        
"""
Model that retrieves the order object, item object and quantity
and return the quantity, name and price
"""
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, null=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.item.name, self.item.price)