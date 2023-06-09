from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase


class EventListViewTests(APITestCase):
    """
    Tests for the Event model list view
    """

    def setUp(self):
        User.objects.create_user(username='user1', password='pass1')

    def test_can_list_events(self):
        user1 = User.objects.get(username='user1')
        Event.objects.create(user=user1, title='test title')
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
