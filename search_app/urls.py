from django.urls import path, include
from .views import do_menu_search, do_recipe_search

urlpatterns=[
    path('result/menu', do_menu_search, name='do_menu_search'),
    path('result/recipe', do_recipe_search, name='do_recipe_search')
]