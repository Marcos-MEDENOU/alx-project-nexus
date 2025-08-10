from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'nexus_orders', views.OrderViewSet, basename='order')
router.register(r'nexus_cart', views.CartViewSet, basename='cart')
router.register(r'nexus_cart_items', views.CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('', include(router.urls)),
]