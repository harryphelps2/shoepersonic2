from decimal import Decimal
from django.shortcuts import get_object_or_404
from shop.models import Shoe


def basket_contents(request):
    """
    Display basket contents on any page
    """
    basket = request.session.get('basket', {})

    basket_items = []
    total = 0
    product_count = 0
    #make quantity into dictionry of size and quantity
    for line_id, line_info in basket.items():
        line_details = line_id.split("-")
        product_id = int(line_details[0])
        size = Decimal(line_details[1]).quantize(Decimal('0.1'))
        product = get_object_or_404(Shoe, pk=product_id)
        quantity = int(line_info['quantity'])
        total += quantity * product.price
        #total += info['quantity'] * product.price

        product_count += quantity
        basket_items.append({'id': product.id, 'quantity': quantity, 'product': product, 'size': size })
    
    return {'basket_items': basket_items, 'total': total, 'product_count': product_count}