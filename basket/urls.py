from django.urls import re_path, path, include, reverse_lazy
from .views import view_basket, add_to_basket, adjust_basket

urlpatterns = [
    path('', view_basket, name="view_basket"),
    re_path(r'^add/(?P<id>\d+)', add_to_basket, name='add_to_basket'),
    re_path(r'^adjust/(?P<id>\d+)/(?P<size>\d+\.\d{1})', adjust_basket, name='adjust_basket'),
]