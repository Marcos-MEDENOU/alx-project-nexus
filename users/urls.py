from django.urls import path
from .views import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserProfileAPIView,
    UserAPIView,
    EmailVerificationAPIView,
    ResendVerificationEmailAPIView
)

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('userdetail/', UserAPIView.as_view(), name='user-detail'),
    path('verify-email/<str:uidb64>/<str:token>/',
         EmailVerificationAPIView.as_view(),
         name='verify-email'),
    path('resend-verification-email/',
         ResendVerificationEmailAPIView.as_view(), 
         name='resend-verification-email'),
]