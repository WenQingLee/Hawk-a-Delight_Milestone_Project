from django.contrib import admin
from .models import Review, MenuItem

# Register your models here.

# Adding the review model to admin interface
admin.site.register(Review)

# Adding the menu_item model to admin interface
admin.site.register(MenuItem)