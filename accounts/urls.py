from django.urls import path, include, reverse_lazy
from . import urls_reset
from .views import user_login, user_logout, user_registration, view_profile, edit_profile
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('register/', user_registration, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'), 
    path('password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"), 
    path('view_profile/', view_profile, name='view_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]