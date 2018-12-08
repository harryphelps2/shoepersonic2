from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileForm, UserForm
from .models import Profile
from checkout.models import Order, OrderLineItem
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

@login_required
def view_profile(request):
    """
    View to show past orders and profile details
    """
    # form with all the profile fields prepoluated
    if request.user.is_authenticated:
        user = request.user
        past_orders =  Order.objects.filter(user = user.id)
        past_order_details = []
        past_order_dates = []
        profile_details = { 
            'marketing_opt_in' : user.profile.marketing_opt_in, 
            'running_club': user.profile.running_club,
            'address_line_1' : user.profile.address_line_1,
            'address_line_2' : user.profile.address_line_2,
            'address_line_3' : user.profile.address_line_3,
            'town_or_city' : user.profile.town_or_city,
            'county' : user.profile.county,
            'postcode' : user.profile.postcode
        }
        user_details = {
            'email' : user.email,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
        }
        profile_form = ProfileForm(profile_details)
        user_form = UserForm(user_details)
        for order in past_orders:
            order_id = order.id
            try:
                line = OrderLineItem.objects.get(order=order_id)
                past_order_details.append(line)
            except OrderLineItem.DoesNotExist:
                line = None      
        return render(request, 'profile.html', {
            'user' : user, 
            'past_orders' : past_orders,
            'past_order_details': past_order_details,
            'profile_form' : profile_form,
            'user_form' : user_form
            })
    else:
        return redirect(reverse('user_login'))

@login_required
def edit_profile(request):
    """
    View to edit profile details 
    """
    user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        user_form = UserForm(request.POST)
        if profile_form.is_valid() and user_form.is_valid:
            user_profile = Profile.objects.get(pk=user.id)
            profile = ProfileForm(request.POST, instance=request.user.profile)
            user_form = UserForm(request.POST, instance=request.user)
            user_form.save()
            profile.save()
            messages.success(request, "You have updated your details")
            return redirect(reverse('view_profile'))
        else:
            messages.error(request, "Could not update your details please try again.")
    else: 
        return redirect(reverse('view_profile'))

    