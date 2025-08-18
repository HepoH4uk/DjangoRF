from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CourseViewSet, LessonListCreateAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonViewSet
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r"courses", CourseViewSet, basename="courses")
router.register(r"lessons", LessonViewSet, basename="lessons")

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls