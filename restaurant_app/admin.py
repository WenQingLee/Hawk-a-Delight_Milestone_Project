from django.contrib import admin
from .models import review

# Register your models here.

# Adding the review model to admin interface
admin.site.register(review)