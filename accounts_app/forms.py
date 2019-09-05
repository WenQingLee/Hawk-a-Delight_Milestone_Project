from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# Login form for users
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
# Registration form for new users    
class UserRegistrationForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label="Password Confirmation")
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
    
    
    # To clean the email input and check if it already exists
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        user = User.objects.filter(email=email)
        
        if user.exists() is True:
            raise ValidationError("This email is already in use. Please try another email.")
            
        return email
        
    # To clean the password input and ensure that both passwords are the same
    def clean_password2(self):
        
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise ValidationError("Please ensure that both the passwords are the same.")
        
        if not password1 or not password2:
            raise ValidationError("Please enter your password twice")
            
        return password2
        
# Reset password form for users
class ResetPasswordForm(forms.Form):

    email = forms.EmailField()