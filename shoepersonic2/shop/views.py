from django.shortcuts import render
from .models import Shoe, Stock, ProductImage, CustomerReview

def all_shoes(request):
    """
    View to show all shoes.
    """
    all_shoes = Shoe.objects.all().order_by('weight_ranking')
    lightweight = Shoe.objects.exclude(weight_ranking__gt=3)
    supportive = Shoe.objects.exclude(weight_ranking__lte=3)
    return render(request, 'all_shoes.html', {'all_shoes':all_shoes, 'lightweight': lightweight, 'supportive': supportive })

def shoe_detail(request, id):
    """
    View to show detailed information about shoe and add to cart
    """
    shoe = Shoe.objects.get(pk=id)
    stock_level = Stock.objects.filter(shoe_model = shoe.id)
    images = ProductImage.objects.filter(shoe_model = shoe.id)
    reviews = CustomerReview.objects.filter(shoe_model = shoe.id)
    return render(request, 'shoe_detail.html', 
                        {
                            'shoe':shoe, 
                            'stock_level':stock_level, 
                            'images':images,
                            'reviews':reviews,
                        })

def add_review(request, id):
    """Add review page"""
    shoe = Shoe.objects.get(pk=id)
    return render(request, 'add_review.html', {'shoe':shoe})