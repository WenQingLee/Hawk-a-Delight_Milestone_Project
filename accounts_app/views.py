from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm

# Create your views here.

# Show the index page
def index(request):
    return render(request, "index.html")

# Logs the user out and return to the index page
def logout(request):
    """
    Logs the user out and show a message if it is successful
    """
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))

# Show the login page
def login(request):
    # Use the UserLoginForm from forms.py
    login_form=UserLoginForm
    return render(request, "login.html", {
        'login_form': login_form
    })