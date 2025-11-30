from django.core.mail import send_mail

from celery import shared_task
from django.utils import timezone
from dateutil.relativedelta import relativedelta

from config.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_update_course(email, course):
    """Отправка сообщения пользователям об обновлении курса"""

    send_mail(
        f"Обновление курса - {course}",
        f"Материалы на курсе ({course}) обновились",
        EMAIL_HOST_USER,
        [email],
    )


@shared_task
def block_user_month():
    """Блокировка пользователей, которые не заходили больше месяца"""

    today_minus_month = timezone.now().today().date() - relativedelta(months=1)
    users_to_block = User.objects.filter(
        is_active=True, last_login__lt=today_minus_month
    )
    users_to_block.update(is_active=False)
