from django.urls import path, include
from.views import index, logout, login, register, password_reset, profile

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('password_reset/', password_reset, name="password_reset"),
    path('profile/', profile, name="profile")
    ]