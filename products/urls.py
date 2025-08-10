from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'nexus_categories', views.CategoryViewSet, basename='category')
router.register(r'nexus_brands', views.BrandViewSet, basename='brand')
router.register(r'nexus_products', views.ProductViewSet, basename='product')
router.register(r'nexus_product_images', views.ProductImageViewSet, basename='product-image')
router.register(r'nexus_product_variants', views.ProductVariantViewSet, basename='product-variant')
router.register(r'nexus_product_attributes', views.ProductAttributeViewSet, basename='product-attribute')
router.register(r'nexus_product_attribute_values', views.ProductAttributeValueViewSet, basename='product-attribute-value')
router.register(r'nexus_product_variant_attributes', views.ProductVariantAttributeViewSet, basename='product-variant-attribute')
router.register(r'nexus_product_reviews', views.ProductReviewViewSet, basename='product-review')
router.register(r'nexus_product_specifications', views.ProductSpecificationViewSet, basename='product-specification')


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