from django.urls import path, include
from .views import all_menu_items, menu_item_detail, menu_type

urlpatterns=[
    path('menu-items/', all_menu_items, name="all_menu_items"),
    path("menu_item_detail/<pk>", menu_item_detail, name="menu_item_detail"),
    path('recipe/menu-type/<type>', menu_type, name="menu_type"),
]