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

router = DefaultRouter()
router.register(r"courses", CourseViewSet)
router.register(r"users", PaymentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('materials.urls', namespace='materials')),
    path("api/payments/", include("users.urls")),
    path("api/", include(router.urls)),
    path("api/lessons/", LessonListCreateAPIView.as_view(), name="lesson_list"),
    path(
        "api/lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_detail"
    ),
    path(
        "api/lessons/<int:pk>/update/",
        LessonUpdateAPIView.as_view(),
        name="lesson_update",
    ),
    path(
        "api/lessons/<int:pk>/delete/",
        LessonDestroyAPIView.as_view(),
        name="lesson_delete",
    ),] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)