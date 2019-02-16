from django.urls import path, re_path, include, reverse_lazy
from home import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    # path('terms_and_conditions', terms_and_conditions, name="terms_and_conditions"),
    # path('privacy_policy', privacy_policy, name="privacy_policy"),
    # path('delivery_and_returns', delivery_and_returns, name="delivery_and_returns"),
    # path('about_us', about_us, name="about_us"),
    # path('faqs', faqs, name="faqs"),
    # path('our_reviews', our_reviews, name="our_reviews"),
]