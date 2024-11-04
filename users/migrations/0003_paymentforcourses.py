# Generated by Django 5.1.1 on 2024-10-10 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentForCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(help_text='Укажите сумму оплаты курса', verbose_name='Сумма оплаты курса')),
                ('session_id', models.CharField(blank=True, help_text='Укажите Id сессии', max_length=255, null=True, verbose_name='Id сессии')),
                ('payment_link', models.URLField(blank=True, help_text='Укажите ссылку на оплату', max_length=400, null=True, verbose_name='Ссылка на оплату')),
                ('user', models.ForeignKey(blank=True, help_text='Укажите пользователя', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Оплата курса',
                'verbose_name_plural': 'Оплата курсов',
            },
        ),
    ]
