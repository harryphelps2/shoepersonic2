from django.urls import path, re_path, include, reverse_lazy
from .views import article_index

urlpatterns = [
    path('', article_index, name="article_index"),
]