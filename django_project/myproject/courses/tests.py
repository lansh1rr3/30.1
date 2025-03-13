from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Course, Lesson, Subscription
from users.models import CustomUser
from django.contrib.auth.models import Group


class LessonAndSubscriptionTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='user@example.com',
            password='test123'
        )
        self.moderator = CustomUser.objects.create_user(
            email='mod@example.com',
            password='test123'
        )
        self.group = Group.objects.create(name='Moderators')
        self.moderator.groups.add(self.group)

        self.course = Course.objects.create(title='Test Course', owner=self.user)
        self.lesson = Lesson.objects.create(
            title='Test Lesson',
            description='Initial description',
            video_url='https://youtube.com/test',
            course=self.course,
            owner=self.user
        )

    def test_lesson_create_as_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('lesson-create')
        data = {
            'title': 'New Lesson',
            'video_url': 'https://youtube.com/new',
            'course': self.course.id,
            'description': 'Test description'
        }
        response = self.client.post(url, data, format='json')
        print("Response for create:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_create_invalid_url(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('lesson-create')
        data = {
            'title': 'Invalid Lesson',
            'video_url': 'https://example.com/video',
            'course': self.course.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_lesson_update_as_moderator(self):
        self.client.force_authenticate(user=self.moderator)
        url = reverse('lesson-update', kwargs={'pk': self.lesson.id})
        data = {'title': 'Updated Lesson'}
        response = self.client.patch(url, data, format='json')
        print("Response for update:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscription_add(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка добавлена')

    def test_subscription_remove(self):
        self.client.force_authenticate(user=self.user)
        Subscription.objects.create(user=self.user, course=self.course)
        url = reverse('subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка удалена')
