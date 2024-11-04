from django.urls import path

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView, PaymentForCoursesCreateAPIView

router = SimpleRouter()
router.register('', PaymentViewSet)

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('users/', UserListAPIView.as_view(), name='users'),
    path('users/<int:pk>/', UserRetrieveAPIView.as_view(), name='users_retrieve'),
    path('users/<int:pk>/update/', UserUpdateAPIView.as_view(), name='users_update'),
    path('users/<int:pk>/delete/', UserDestroyAPIView.as_view(), name='users_delete'),

    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path('payment_for_courses/', PaymentForCoursesCreateAPIView.as_view(), name='payment_for_courses'),
] + router.urls
