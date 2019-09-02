from django.db import models
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField
    preparation_steps = models.TextField
    category = models.CharField(max_length=100)
    duration = models.IntegerField
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    review = models.ForeignKey('Review', on_delete=models.CASCADE)
    
    
class Review(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name