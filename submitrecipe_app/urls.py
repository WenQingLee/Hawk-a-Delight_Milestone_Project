from django.urls import path, include
from .views import submit_recipe, recipe_list, recipe_details, submit_review, upvote_recipe, edit_recipe, edit_review, delete_recipe, delete_review

urlpatterns = [
    path('recipe/', submit_recipe, name='submit_recipe'),
    path('recipe/list/', recipe_list, name='recipe_list'),
    path('recipe/details/<int:id>', recipe_details, name='recipe_details'),
    path('recipe/review/<int:id>', submit_review, name='submit_review'),
    path('recipe/upvote/<int:id>', upvote_recipe, name='upvote_recipe'),
    path('recipe/edit-recipe/<int:id>', edit_recipe, name='edit_recipe'),
    path('recipe/edit-review/<int:id>', edit_review, name='edit_review'),
    path('recipe/delete-recipe/<int:id>', delete_recipe, name='delete_recipe'),
    path('recipe/delete-review/<int:id>', delete_review, name="delete_review")
    ]