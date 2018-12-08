from django.urls import path, re_path, include, reverse_lazy
from .views import articles, do_you_need_spikes

urlpatterns = [
    path('', articles, name="articles"),
    path('do_you_need_spikes/', do_you_need_spikes, name="do_you_need_spikes")
]