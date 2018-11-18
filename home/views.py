from django.shortcuts import render

def index(request):
    """Homepage view"""
    return render(request, 'index.html')

def terms_and_conditions(request):
    """terms_and_conditions view"""
    return render(request, 'terms_and_conditions.html')

def privacy_policy(request):
    """privacy_policy view"""
    return render(request, 'privacy_policy.html')

def delivery_and_returns(request):
    """delivery_and_returns view"""
    return render(request, 'delivery_and_returns.html')

def about_us(request):
    """About us view"""
    return render(request, 'about_us.html')

def faqs(request):
    """FAQS view"""
    return render(request, 'faqs.html')

def our_reviews(request):
    """our_reviews view"""
    return render(request, 'our_reviews.html')