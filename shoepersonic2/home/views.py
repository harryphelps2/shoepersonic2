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

