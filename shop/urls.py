from django.urls import path, re_path, include, reverse_lazy
from .views import all_shoes, shoe_detail

urlpatterns = [
    path('all_shoes/', all_shoes, name="all_shoes"),
    re_path(r'^shoe_detail/(?P<id>\d+)/$', shoe_detail, name='shoe_detail'),
]