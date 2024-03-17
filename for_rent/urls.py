"""
URL configuration for for_rent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import include, path

from authApi.views import authiView
from property_api.views import PropertyClassViewSet
from reviews_api.views import ReviewViewSet
from rest_framework.routers import DefaultRouter
from authApi.views import authiView, LoginView
from users_api import urls as app_urls
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r"properties", PropertyClassViewSet, basename="properties")
router.register(r"register", authiView, basename="register")
router.register(r"reviews", ReviewViewSet, basename="review-list")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("login/", LoginView.as_view(), name="login"),
    path('api/', include(app_urls)),
    path("", include(router.urls)),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)