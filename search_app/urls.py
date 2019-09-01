from django.urls import path, include
from .views import do_search

urlpatterns=[
    path('result/', do_search, name='do_search')    
]