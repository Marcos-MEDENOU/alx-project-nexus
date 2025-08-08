"""
URL configuration for masebuy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from django.views.generic import RedirectView
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="Nexus API- Ecommerce",
        default_version='v1',
        description="Nexus Ecommerce API documentation",
        terms_of_service="https://www.nexus.com/terms/",
        contact=openapi.Contact(email="marcosmedenou@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', RedirectView.as_view(url='swagger/')),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('users.urls')),
    # path('api/v1/auth/', include('knox.urls')),
    # path('api/v1/', include('products.urls')),
    # path('api/v1/', include('orders.urls')),
    # path('api/v1/', include('payments.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<path>.*)$', serve, {
            'document_root': os.path.join(settings.STATIC_ROOT, 'drf-yasg'),
        }),
    ]
