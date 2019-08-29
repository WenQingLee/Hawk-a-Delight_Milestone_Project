from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# Login form for users
class UserLoginForm(forms.Form):
    """Form to login user using username and password"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
# Registration form for new users    
class UserRegistrationForm(UserCreationForm):
    """
    Input fields for password and confirm password with a widget for 
    PasswordInput class to obscure the password
    """
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label="Password Confirmation")
    
    """
    Format of the user registration form to follow the user from
    django.contrib.auth.models with the required fields of email,
    username, password1 and password2
    """
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    