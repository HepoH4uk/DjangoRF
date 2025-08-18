from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CourseViewSet, LessonListCreateAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonViewSet, SubscriptionAPIView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register(r"courses", CourseViewSet, basename="courses")
router.register(r"lessons", LessonViewSet, basename="lessons")

urlpatterns = [
    path('', include(router.urls)),
    path("subscriptions/", SubscriptionAPIView.as_view(), name="subscriptions"),
]

urlpatterns += router.urls