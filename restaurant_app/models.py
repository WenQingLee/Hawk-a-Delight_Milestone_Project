from django.db import models
from django.utils import timezone

# Create your models here.
class review(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
