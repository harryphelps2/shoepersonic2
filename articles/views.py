from django.shortcuts import render

def article_index(request):
    """
    View to Render the index page of our
    articles (also called the Hangar)
    """
    return render(request, 'article_index.html')
