from django.contrib import admin
from django.urls import include, path
from payment_api.views import PaymentViewSet
from requests_api.views import RequestViewSet
from reviews_api.views import ReviewViewSet
from authApi.views import VerifyCode, authiView
from property_api.views import PropertyClassViewSet
from rest_framework.routers import DefaultRouter
from authApi.views import authiView, LoginView
from django.conf import settings
from django.conf.urls.static import static
from users_api.views import UserViewSet

router = DefaultRouter()
router.register(r"properties", PropertyClassViewSet, basename="properties")
router.register(r"properties/search", PropertyClassViewSet, basename="properties-search")
router.register(r"register", authiView, basename="register")
router.register(r"reviews", ReviewViewSet, basename="review-list")
router.register(r"users", UserViewSet, basename="user")
router.register(r"requests", RequestViewSet, basename="requests")
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("login/", LoginView.as_view(), name="login"),
    path("verify/", VerifyCode.as_view(), name="verify"),
    path("api/", include('users_api.urls')),
    path("properties/search/", PropertyClassViewSet.as_view({"get": "list"}), name="properties-search"),
    path("", include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
