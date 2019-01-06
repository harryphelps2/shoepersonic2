from django.urls import re_path, path, include, reverse_lazy
from .views import contact_details, delivery_details, submit_order, card_details, order_submitted

urlpatterns = [
    path('contact_details', contact_details, name="contact_details"),
    path('delivery_details', delivery_details, name="delivery_details"),
    path('card_details', card_details, name="card_details"),
    path('submit_order', submit_order, name="submit_order"),
    path('order_submitted/<int:order_id>/', order_submitted, name='order_submitted')
]