from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from materials.models import Lesson, Course, CourseSubscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='new_test@test.ru')
        self.course = Course.objects.create(name='Самый самый новый курс', course_description='Самый самый новый курс!')
        self.lesson = Lesson.objects.create(name='Самый новый урок', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lessons_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse('materials:lessons_create')
        data = {
            "name": "Новый новый урок",
            "course": self.course.pk,
            "video_link": "http://www.youtube.com/Новый"
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.count(), 2
        )

    def test_lesson_update(self):
        url = reverse('materials:lessons_update', args=(self.lesson.pk,))
        data = {
            "name": "Новый новый тест",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), "Новый новый тест"
        )

    def test_lesson_delete(self):
        url = reverse('materials:lessons_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.count(), 0
        )

    def test_lesson_list(self):
        url = reverse('materials:lessons_list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = {'count': 1, 'next': None, 'previous': None, 'results': [
            {'id': self.lesson.pk, 'video_link': '', 'name': self.lesson.name, 'description': None,
             'preview_image': None,
             'course': self.course.pk, 'owner': self.user.pk}]}
        self.assertEqual(
            data, result
        )


class CourseSubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='new_test@test.ru')
        self.course = Course.objects.create(name='Самый самый новый курс')
        self.client.force_authenticate(user=self.user)

    def test_subscribe_to_course(self):
        url = reverse('materials:course_subscription')
        response = self.client.post(url, {'course_id': self.course.pk})
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data['message'], 'подписка добавлена'
        )
        # self.assertTrue(CourseSubscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_to_course(self):
        CourseSubscription.objects.create(user=self.user, course=self.course)
        url = reverse('materials:course_subscription')
        response = self.client.post(url, {'course_id': self.course.pk})
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data['message'], 'подписка удалена'
        )
