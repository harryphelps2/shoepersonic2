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

def returns(request):
    """Returns view"""
    return render(request, 'returns.html')

def delivery_options(request):
    """Delivery options view"""
    return render(request, 'delivery_options.html')

def about_us(request):
    """About us view"""
    return render(request, 'about_us.html')

def contact_us(request):
    """Contact us view"""
    return render(request, 'contact_us.html')

def faqs(request):
    """FAQS view"""
    return render(request, 'faqs.html')

def our_reviews(request):
    """our_reviews view"""
    return render(request, 'our_reviews.html')