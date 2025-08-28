from datetime import timedelta
from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.utils import timezone

from materials.models import Course, Subscription


@shared_task
def send_course_update_notification(course_id):
    course = Course.objects.get(id=course_id)
    subscribers = Subscription.objects.filter(course=course, is_active=True)

    for subscription in subscribers:
        send_mail(
            subject=f"Обновление курса: {course.title}",
            message=f"Курс {course.title} обновлен!",
            from_email=EMAIL_HOST_USER,
            recipient_list=[subscription.user.email],
            fail_silently=False,
        )


@shared_task
def send_lesson_update_notification(lesson_id):
    from materials.models import Lesson, Subscription

    lesson = Lesson.objects.get(id=lesson_id)
    course = lesson.course

    if course.updated_at < timezone.now() - timedelta(hours=4):
        subscribers = Subscription.objects.filter(course=course, is_active=True)

        for subscription in subscribers:
            send_mail(
                subject=f"Обновление урока в курсе: {course.title}",
                message=f"Урок '{lesson.title}' в курсе {course.title} обновлен!",
                from_email=EMAIL_HOST_USER,
                recipient_list=[subscription.user.email],
                fail_silently=False,
            )
