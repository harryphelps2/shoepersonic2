from django.shortcuts import render
from .models import Shoe, Stock, ProductImage, CustomerReview
from .forms import CommentForm
from django.utils import timezone

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
    comment_form = CommentForm()
    if request.method == 'POST':
        comment = CommentForm(request.POST).save(commit=False)
        comment.shoe_model = shoe
        comment.date = timezone.now()
        comment.user = request.user
        comment.save()
    return render(request, 'shoe_detail.html', 
                        {
                            'shoe':shoe, 
                            'stock_level':stock_level, 
                            'images':images,
                            'reviews':reviews,
                            'comment_form':comment_form,
                        })

# def add_review(request, id):
#     """Add review page"""
#     shoe = Shoe.objects.get(pk=id)
#     if request.PO
#     return render(request, 'add_review.html', {'shoe':shoe})