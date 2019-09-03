from django.urls import path, include
from .views import submit_recipe, recipe_list, recipe_details

urlpatterns = [
    path('recipe/', submit_recipe, name='submit_recipe'),
    path('recipe/list/', recipe_list, name='recipe_list'),
    path('recipe/details/<int:id>', recipe_details, name='recipe_details')
    ]