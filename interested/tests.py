from django.contrib.auth.models import User
from events.models import Event
from .models import Interested
from rest_framework import status
from rest_framework.test import APITestCase


class InterestedListViewTests(APITestCase):
    """
    Tests for the Interested list view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        event1 = Event.objects.create(
            user=user1,
            title='event',
            country='Germany'
        )

    def test_can_list_interested(self):
        user1 = User.objects.get(username='user1')
        event1 = Event.objects.get(pk=1)
        Interested.objects.create(
            user=user1,
            event=event1,
        )
        response = self.client.get('/interested/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_interested_for_an_event(self):
        self.client.login(username='user1', password='pass1')
        event1 = Event.objects.get(pk=1)
        user1 = User.objects.get(username='user1')
        response = self.client.post(
            '/interested/', {
                'user': user1,
                'event': 1,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_interested_for_an_event(self):
        event1 = Event.objects.get(pk=1)
        response = self.client.post(
            '/interested/', {
                'event': 1,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
