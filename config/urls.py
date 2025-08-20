from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from config import settings
from materials.views import (
    CourseViewSet,
    LessonListCreateAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
)
from users.views import PaymentViewSet

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r"courses", CourseViewSet)
router.register(r"users", PaymentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('materials.urls', namespace='materials')),
    path("users/", include("users.urls", namespace='users')),
    path("payments/", include("users.urls")),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)