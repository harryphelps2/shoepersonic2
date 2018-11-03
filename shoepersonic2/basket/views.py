from django.shortcuts import render, redirect, reverse

def view_basket(request):
    """A view that renders the cart contents"""
    basket = request.session.get('cart', {})
    return render(request, "basket.html")

def add_to_cart(request, id):
    """Add a quantity product to cart"""
    # build in check that stops them submitting if they don't select size
    
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')
    line_id = "{0}-{1}".format(id, size)

    basket = request.session.get('basket', {})

    if line_id not in basket:
        basket[line_id] = {
            'quantity': 0,
            'size': size
        }

    basket[line_id]["quantity"] += quantity

    request.session['basket'] = cart

    return redirect(reverse('view_basket'))

def adjust_basket(request, id, size):
    """Adjust quantity of the product to the specified amount"""
    quantity = int(request.POST.get('new_quantity'))
    basket = request.session.get('basket', {})
    line_id = "{0}-{1}".format(id, size)

    if quantity > 0:
        basket[line_id]["quantity"] = quantity
    else:
        basket.pop(line_id)
    
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))