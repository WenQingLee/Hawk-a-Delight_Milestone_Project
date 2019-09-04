from django.db import models
from django.utils import timezone

# Create your models here.

# Model for restaurant menu items
class MenuItem(models.Model):
    name = models.CharField(max_length=300, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    type = models.CharField(
        max_length=100,
        choices= [
            ("Breakfast", "Breakfast"),
            ("Lunch", "Lunch"),
            ("Dinner", "Dinner")
            ],
        default="Breakfast"
        )
    
    def __str__(self):
        return self.name
