from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payment, User, PaymentForCourses


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaymentForCoursesSerializer(ModelSerializer):
    class Meta:
        model = PaymentForCourses
        fields = '__all__'
