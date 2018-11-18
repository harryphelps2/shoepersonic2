from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include, reverse_lazy

urlpatterns = [
    path('', PasswordResetView.as_view(), name="password_reset"),
    path('done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"), 
]