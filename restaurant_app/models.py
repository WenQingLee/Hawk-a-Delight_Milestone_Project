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
