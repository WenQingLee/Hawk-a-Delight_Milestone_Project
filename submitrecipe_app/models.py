from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.

# Model for user submitted recipes
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    duration = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    image = ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
# Model for reviews for submitted recipes
class Review(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.name