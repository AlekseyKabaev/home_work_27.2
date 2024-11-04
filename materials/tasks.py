from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from datetime import timedelta

from config.settings import EMAIL_HOST_USER
from materials.models import CourseSubscription, Course
from users.models import User


@shared_task
def send_course_update_email(course_pk):
    """Отправляет сообщение пользователю об обновлении материалов курса."""
    course = Course.objects.get(pk=course_pk)
    subscribed_course = CourseSubscription.objects.filter(course=course)
    for sub in subscribed_course:
        send_mail('Обновление материалов курса',
                  'Сообщаем вам, что материалы курса обновились!', EMAIL_HOST_USER,
                  [sub.user.email])


@shared_task
def block_inactive_users():
    users = User.objects.filter(last_login__isnull=False)
    today = timezone.now()

    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f'Пользователь {user.email} отелючен')
        else:
            print(f'Пользователь {user.email} активен')
