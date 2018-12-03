from django.urls import path, re_path, include, reverse_lazy
from .views import all_shoes, shoe_detail, add_comment_for_shoe, edit_comment_for_shoe, delete_comment_for_shoe

urlpatterns = [
    path('all_shoes/', all_shoes, name="all_shoes"),
    re_path(r'^shoe_detail/(?P<id>\d+)/$', shoe_detail, name='shoe_detail'),
    re_path(r'^add_comment_for_shoe/(?P<id>\d+)/$', add_comment_for_shoe, name='add_comment_for_shoe'),
    re_path(r'^edit_comment_for_shoe/(?P<id>\d+)/$', edit_comment_for_shoe, name='edit_comment_for_shoe'),
    re_path(r'^delete_comment_for_shoe/(?P<id>\d+)/$', delete_comment_for_shoe, name='delete_comment_for_shoe'),
]