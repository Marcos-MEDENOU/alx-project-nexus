from django.urls import path
from .views import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserLogoutAllAPIView,
    UserProfileAPIView,
    UserAPIView,
    EmailVerificationAPIView,
    ResendVerificationEmailAPIView
)

urlpatterns = [
    path('nexus_register/', UserRegistrationAPIView.as_view(), name='register'),
    path('nexus_login/', UserLoginAPIView.as_view(), name='login'),
    path('nexus_logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('nexus_logout-all/', UserLogoutAllAPIView.as_view(), name='logout-all'),
    path('nexus_profile/', UserProfileAPIView.as_view(), name='profile'),
    path('nexus_me/', UserAPIView.as_view(), name='user-detail'),
    path('nexus_verify-email/<str:uidb64>/<str:token>/',
         EmailVerificationAPIView.as_view(),
         name='verify-email'),
    path('nexus_resend-verification-email/',
         ResendVerificationEmailAPIView.as_view(), 
         name='resend-verification-email'),
]