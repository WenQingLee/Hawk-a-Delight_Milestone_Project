from django.urls import path, include
from .views import all_menu_items, get_reviews, review_detail, create_edit_review

urlpatterns=[
    path('menu-items/', all_menu_items, name="all_menu_items"),
    path('reviews/', get_reviews, name='get_reviews'),
    path("reviews/<pk>", review_detail),
    path("reviews/form/<pk>", create_edit_review),
]