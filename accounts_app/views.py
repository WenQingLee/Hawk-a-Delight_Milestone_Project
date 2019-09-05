from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, ResetPasswordForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Allows the user to register in the index page
def index(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
           
            user = auth.authenticate(username = request.POST['username'], password = request.POST['password1'])
            if user is not None:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully signed up for an account")
                return redirect(reverse('all_menu_items'))
            else:
                messages.error(request, "We are unable to create your account, please try again")
        else:
            return render(request, 'register.html', {
                'form': form
            })
            
    form = UserRegistrationForm()
    
    return render(request, "index.html", {
        'form': form
    })

# Logs the user out and show a success message before returning to the index page
@login_required()
def logout(request):
    
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect(reverse('index'))

# Allows the user to login
def login(request):
    
    if request.method == 'POST':

        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            
            """
            Check if the username and password is correct
            and show a message if it is successful
            """
            user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
            
            if user is not None:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('all_menu_items'))
              
            else:
                login_form.add_error(None, 'Invalid username or password')
                
        return render(request, 'login.html', {
            'login_form':login_form
        })
            
    else:
        
        login_form=UserLoginForm
        
        return render(request, "login.html", {
            'login_form': login_form
        })
        
# Allows the user to register and show a messsage and index message if successful
def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            user = auth.authenticate(username = request.POST['username'], password = request.POST['password1'])
            if user is not None:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully signed up for an account")
                return redirect(reverse('index'))
            else:
                messages.error(request, "We are unable to create your account, please try again")
        else:
            return render(request, 'register.html', {
                'form': form
            })
    
    form = UserRegistrationForm()
    
    return render(request, 'register.html', {
        'form': form
    })

# Show the password reset page
def password_reset(request):
    reset_password_form=ResetPasswordForm
    return render(request, "password-reset.html", {
        'reset_password_form': reset_password_form
    })
    
# Show the user profile page
@login_required()
def profile(request):
    profile = request.user
    return render(request, "profile.html", {
        'profile':profile
    })
    