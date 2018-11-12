from django.urls import path, re_path, include, reverse_lazy
from .views import index, terms_and_conditions, privacy_policy

urlpatterns = [
    path('', index, name="index"),
    path('terms_and_conditions', terms_and_conditions, name="terms_and_conditions"),
    path('privacy_policy', privacy_policy, name="privacy_policy"),
]