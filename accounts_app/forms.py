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
    Added first names and last names as the required field in the registration form
    """
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
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
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
    
    
    # To clean the email input and check if it already exists
    def clean_email(self):
        """
        Extracts the email from the registration form and process
        it to normalise it to a consistent format
        """
        email = self.cleaned_data.get('email')
        
        """
        Check if there is any user using the same email and assign
        it to user
        """
        user = User.objects.filter(email=email)
        
        """
        If the queryset(user) contains any results returns True, if not,
        False. If True, raise an error that it is already in use.
        """
        if user.exists() is True:
            raise ValidationError("This email is already in use. Please try another email.")
            
        return email
        
    # To clean the password input and ensure that both passwords are the same
    def clean_password2(self):
        """
        Extracts the password from the registration form and process
        it to normalise it to a consistent format
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        """
        If the passwords don't match, raise an error.
        """
        if password1 != password2:
            raise ValidationError("Please ensure that both the passwords are the same.")
        
        """
        If any of the inputs for the password are missing, raise an error
        """
        if not password1 or not password2:
            raise ValidationError("Please enter your password twice")
            
        return password2
        
# Reset password form for users
class ResetPasswordForm(forms.Form):
    """Form for user to reset password"""
    email = forms.EmailField()