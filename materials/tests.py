from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test5@test.com",
            password="123qwe")

        self.course = Course.objects.create(
            name="Course 1",
            owner=self.user)

        self.lesson = Lesson.objects.create(
            name="Lesson 1",
            course=self.course,
            owner=self.user)

        self.client.force_authenticate(user=self.user)


    def test_get_lessons_list(self):
        Lesson.objects.create(
            name="Lesson 1",
            course=self.course,
            owner=self.user,
            video_url="https://www.youtube.com/test",
        )
        url = reverse("materials:lessons-list")

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_one_lesson(self):
        lesson = Lesson.objects.create(
            name="Test Lesson",
            course=self.course,
            owner=self.user,
            video_url="https://www.youtube.com/watch?v=test",
        )
        url = reverse("materials:lessons-detail", args=[lesson.id])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Lesson")


    def test_lesson_create(self):
        url = reverse("materials:lessons-list")
        lesson = {
            "name": self.lesson,
            "course": self.course.pk,
            "video_url": "https://www.youtube.com/test",
        }
        response = self.client.post(url, lesson)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_lesson_invalid_url(self):
        url = reverse("materials:lessons-list")
        lesson = {
            "name": self.lesson,
            "course": self.course.pk,
            "video_url": "https://www.22134243.com/test",
            }
        response = self.client.post(url, lesson)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    # def test_update_lesson(self):
    #     lesson = {
    #         "name": "Test 4"
    #     }
    #     url = reverse("materials:lessons-detail", args=[self.lesson.pk])
    #     response = self.client.patch(url, lesson)
    #     data = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(data.get("name"), "Test 4")


    def test_delete_lesson(self):

        url = reverse("materials:lessons-detail", args=[self.lesson.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test5@test.com",
            password="123qwe")

        self.course = Course.objects.create(
            name="Course 1",
            owner=self.user)

        self.lesson = Lesson.objects.create(
            name="Lesson 1",
            course=self.course,
            owner=self.user)

        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        Subscription.objects.all().delete()
        url = reverse('materials:subscriptions')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка добавлена')
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())
        url = reverse('materials:subscriptions')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка удалена')
