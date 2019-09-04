from django.db import models
from django.utils import timezone

# Create your models here.

# Model for user submitted reviews for recipes
class Review(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __unicode__(self):
        return self.name

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
