from django.urls import path, re_path, include, reverse_lazy
from .views import all_shoes, shoe_detail, add_review

urlpatterns = [
    path('all_shoes/', all_shoes, name="all_shoes"),
    re_path(r'^shoe_detail/(?P<id>\d+)/$', shoe_detail, name='shoe_detail'),
    re_path(r'^add_review/(?P<id>\d+)/$', add_review, name='add_review'),
]