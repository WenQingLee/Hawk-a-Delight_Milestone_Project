from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Show the index page
def index(request):
    return render(request, "index.html")

# Logs the user out and return to the index page
def logout(request):
    """
    Logs the user out and show a message if it 
    is successful
    """
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))

# Show the login page
def login(request):
    # If the user submits their username and passowrd
    if request.method == 'POST':
        """
        Get the user inputs with reference to the 
        UserLoginForm from forms.py
        """
        login_form = UserLoginForm(request.POST)
        
        """
        Runs validation if the login input fits the 
        form input fields specified
        """
        if login_form.is_valid():
            
            """
            Check if the username and password is correct
            and show a message if it is successful
            """
            user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
            
            """"
            If correct, logs in the user and redirect to the index page,
            otherwise show
            an error message
            """
            if user is not None:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
              
            else:
                login_form.add_error(None, 'Invalid username or password')
        return render(request, 'login.html', {
            'login_form':login_form
        })
            
    else:
        # Use the UserLoginForm from forms.py
        login_form=UserLoginForm
        return render(request, "login.html", {
            'login_form': login_form
        })