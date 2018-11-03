from django.urls import re_path, path, include, reverse_lazy
from .views import checkout

urlpatterns = [
    path('', checkout, name="checkout"),
]