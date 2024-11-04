from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'city')
    list_filter = ('email',)
    search_fields = ('email', 'phone')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'pay_date', 'payed_course', 'payed_lesson', 'payment_amount', 'payment_method')
    list_filter = ('user',)
    search_fields = ('user', 'pay_date', 'payment_method')
