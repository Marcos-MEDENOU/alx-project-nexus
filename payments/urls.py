from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'nexus_payments', views.PaymentViewSet, basename='Nexus Payment')

urlpatterns = [
    path('', include(router.urls)),
    path('nexus_api/v1/payment/', views.MpesaPaymentView.as_view(), name='Nexus Payment'),
    path('nexus_api/v1/callback/', views.MpesaCallbackView.as_view(), name='Nexus Payment Callback'), 
]
 