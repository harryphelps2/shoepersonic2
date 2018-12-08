from django.shortcuts import render

def articles(request):
    """
    View to Render the index page of our
    articles (also called the Hangar)
    """
    return render(request, 'articles.html')

def do_you_need_spikes(request):
    """
    View for blog entry for why a customer needs spikes
    """
    return render(request, 'do-you-need-spikes.html')