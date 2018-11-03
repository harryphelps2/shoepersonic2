from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.context_processors import csrf

def index(request):
    """A view the returns the index page"""
    return (request, 'index.html')

def user_login(request):
    """View that returns the login form"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['email'],
                                        password=request.POST['password'])
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Your username or password is incorrect")
    else:
        user_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': user_form})

@login_required
def user_logout(request):
    auth.logout(request)
    messages.success(request, "You have been successfully logged out. See you soon!")
    return redirect(reverse('index'))

def user_registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method=="POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['email'],
                                     password=request.POST['password1'])                  
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'register.html', {"registration_form": registration_form})
    