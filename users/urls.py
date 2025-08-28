from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from .apps import UsersConfig
from .views import PaymentViewSet, UserCreateAPIView, PaymentCreateAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", PaymentViewSet, basename="payments")

urlpatterns = [
    path("", include(router.urls)),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('donations/', PaymentCreateAPIView.as_view(), name='donations'),
]

urlpatterns += router.urls