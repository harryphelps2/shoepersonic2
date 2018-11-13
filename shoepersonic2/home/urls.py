from django.urls import path, re_path, include, reverse_lazy
from .views import index, terms_and_conditions, privacy_policy, returns, delivery_options, about_us, contact_us, faqs, our_reviews

urlpatterns = [
    path('', index, name="index"),
    path('terms_and_conditions', terms_and_conditions, name="terms_and_conditions"),
    path('privacy_policy', privacy_policy, name="privacy_policy"),
    path('returns', returns, name="returns"),
    path('delivery_options', delivery_options, name="delivery_options"),
    path('about_us', about_us, name="about_us"),
    path('contact_us', contact_us, name="contact_us"),
    path('faqs', faqs, name="faqs"),
    path('our_reviews', our_reviews, name="our_reviews"),
]