from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import ContactDetailsForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from shop.models import Shoe
from .models import OrderLineItem
from shoepersonic2 import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET

def contact_details(request):
    """Collect email and running club and add to session"""
    # If user is authenticated take the email address from
    user = request.user
    if user.is_authenticated:
        # get user object and populate contact form with email and running club
    # user and running club from profile
        contact_details = {'email': user.email, 'running_club': user.profile.running_club }
        contact_form = ContactDetailsForm(contact_details)
    # If the form is valid 
        if request.method == "POST":
            if contact_form.is_valid():
                request.session['email'] = contact_form.cleaned_data['email']
                request.session['running_club'] = contact_form.cleaned_data['running_club']
                return redirect(reverse('delivery_details'))
    else:
        contact_details = {'email' : request.session.get('email', None), 'running_club' : request.session.get('running_club', None)}
        contact_form = ContactDetailsForm(request.POST or contact_details)
        if request.method == "POST":
            print(contact_form)
            if contact_form.is_valid():
                request.session['email'] = contact_form.cleaned_data['email']
                request.session['running_club'] = contact_form.cleaned_data['running_club']
                return redirect(reverse('delivery_details'))
    return render(request, 'contact_details.html', {'contact_form': contact_form})
    # If not get it from the session or from a blank form

    # Add the email to the session and go to step 2


def delivery_details(request):
    """Collect name and address and add to session"""
    return render(request, 'delivery_details.html')

def submit_order(request):
    """Make payment"""
    # if request.method=="POST":
    #     order_form = OrderForm(request.POST)
    #     if order_form.is_valid():
    #         order = order_form.save(commit=False)
    #         order.date = timezone.now()
    #         order.user = request.user.id
    #         order.save()

    #         basket = request.session.get('basket', {})
    #         total = 0
    #         for line_id, line_info in basket.items():
    #             product_id, size = line_id.split("-")
    #             product = get_object_or_404(Shoe, pk=product_id)
    #             stock_level = get_object_or_404(Stock, size=size, shoe_model=product_id)
    #             quantity = line_info['quantity']
    #             if stock_level.stock < quantity:
    #                 messages.error("Oh no there's only {0} left! Please adjust the quantity in your cart.").format(quantity)
    #                 return redirect(reverse('view_basket'))
    #             else:
    #                 stock_level.stock -= quantity
    #                 stock_level.save()
    #             total += quantity * product.price
    #             order_line_item = OrderLineItem(
    #                 order = order,
    #                 product = product,
    #                 quantity = quantity,
    #                 size = size
    #             )
    #             order_line_item.save()
            
    #         try:
    #             token = request.POST['stripeToken'] 
    #             charge = stripe.Charge.create(
    #                 amount=int(total*100),
    #                 currency='gbp',
    #                 description=request.user.email,
    #                 source=token,
    #             )
    #         except stripe.error.CardError:
    #             messages.error(request, "Your card was declined!")
            
    #         if charge.paid:
    #             messages.success(request, "You have successfully paid!")
    #             request.session['basket'] = {}
    #             return redirect(reverse('index'))
    #         else:
    #             messages.error(request, "Unable to take payment.")
    #     else:
    #         messages.error(request, "Unable to take payment on that card")
    # else:
    #     order_form = OrderForm()
    # return render(request, 'checkout.html', {'order_form':order_form})