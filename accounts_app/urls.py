from django.urls import path, include
from.views import index, logout, login, register

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    ]