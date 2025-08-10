from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'nexus_categories', views.CategoryViewSet, basename='Nexus Category')
router.register(r'nexus_brands', views.BrandViewSet, basename='Nexus Brand')
router.register(r'nexus_products', views.ProductViewSet, basename='Nexus Product')
router.register(r'nexus_product_images', views.ProductImageViewSet, basename='Nexus Product Image')
router.register(r'nexus_product_variants', views.ProductVariantViewSet, basename='Nexus Product Variant')
router.register(r'nexus_product_attributes', views.ProductAttributeViewSet, basename='Nexus Product Attribute')
router.register(r'nexus_product_attribute_values', views.ProductAttributeValueViewSet, basename='Nexus Product Attribute Value')
router.register(r'nexus_product_variant_attributes', views.ProductVariantAttributeViewSet, basename='Nexus Product Variant Attribute')
router.register(r'nexus_product_reviews', views.ProductReviewViewSet, basename='Nexus Product Review')
router.register(r'nexus_product_specifications', views.ProductSpecificationViewSet, basename='Nexus Product Specification')


urlpatterns = [
    path('', include(router.urls)),
    path('nexus_products/<slug:slug>/reviews/', 
         views.ProductViewSet.as_view({'get': 'reviews'}), 
         name='product-reviews'),
    path('nexus_products/<slug:slug>/add-review/', 
         views.ProductViewSet.as_view({'post': 'add_review'}), 
         name='add-review'),
    path('nexus_products/<slug:slug>/add-image/', 
         views.ProductViewSet.as_view({'post': 'add_image'}), 
         name='add-image'),
]