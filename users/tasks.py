from datetime import timedelta

from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


@shared_task
def check_user_activity():
    login_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(
        last_login__lt=login_month_ago, is_active=True
    )
    for user in inactive_users:
        user.is_active = False
        user.save()
