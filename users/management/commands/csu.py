from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        email = 'admin1@example.ru'
        password = '123qwe'

        # Создаем суперпользователя
        user = User.objects.create(email=email)

        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Суперпользователь {email} был создан."))
