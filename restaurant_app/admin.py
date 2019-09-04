from django.contrib import admin
from .models import MenuItem

# Register your models here.


# Adding the menu_item model to admin interface
admin.site.register(MenuItem)