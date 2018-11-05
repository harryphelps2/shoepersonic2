from django.urls import re_path, path, include, reverse_lazy
from .views import contact_details, delivery_details, submit_order

urlpatterns = [
    path('contact_details', contact_details, name="contact_details"),
    path('delivery_details', delivery_details, name="delivery_details"),
    path('submit_order', submit_order, name="submit_order"),
]