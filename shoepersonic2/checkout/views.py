from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.contrib import messages
from django.utils import timezone
from shop.models import Shoe
from .models import OrderLineItem
from shoepersonic2 import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET


def checkout(request):
    """Make payment"""
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = request.user.id
            order.save()

            basket = request.session.get('basket', {})
            total = 0
            for line_id, line_info in basket.items():
                product_id, size = line_id.split("-")
                product = get_object_or_404(Shoe, pk=product_id)
                stock_level = get_object_or_404(Stock, size=size, shoe_model=product_id)
                quantity = line_info['quantity']
                if stock_level.stock < quantity:
                    messages.error("Oh no there's only {0} left! Please adjust the quantity in your cart.").format(quantity)
                    return redirect(reverse('view_basket'))
                else:
                    stock_level.stock -= quantity
                    stock_level.save()
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity,
                    size = size
                )
                order_line_item.save()
            
            try:
                token = request.POST['stripeToken'] 
                charge = stripe.Charge.create(
                    amount=int(total*100),
                    currency='gbp',
                    description=request.user.email,
                    source=token,
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            
            if charge.paid:
                messages.success(request, "You have successfully paid!")
                request.session['basket'] = {}
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment.")
        else:
            messages.error(request, "Unable to take payment on that card")
    else:
        order_form = OrderForm()
    return render(request, 'checkout.html', {'order_form':order_form})