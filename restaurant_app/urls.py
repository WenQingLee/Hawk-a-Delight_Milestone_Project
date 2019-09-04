from django.urls import path, include
from .views import all_menu_items, menu_item_detail, menu_type, get_reviews, review_detail, create_edit_review

urlpatterns=[
    path('menu-items/', all_menu_items, name="all_menu_items"),
    path('reviews/', get_reviews, name='get_reviews'),
    path("menu_item_detail/<pk>", menu_item_detail, name="menu_item_detail"),
    path("reviews/<pk>", review_detail),
    path("reviews/form/<pk>", create_edit_review),
     path('recipe/menu-type/<type>', menu_type, name="menu_type"),
]