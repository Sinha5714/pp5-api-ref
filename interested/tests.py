# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal:
from events.models import Event
from .models import Interested
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class InterestedListViewTests(APITestCase):
    """
    Tests for the Interested list view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        event1 = Event.objects.create(
            user=user1,
            title='event',
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


class InterestedDetailViewTests(APITestCase):
    """
    Test for Interested detail view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        user2 = User.objects.create_user(username='user2', password='pass2')

        event1 = Event.objects.create(
            user=user1,
            title='User1 title',
        )
        event2 = Event.objects.create(
            user=user2,
            title='User2 title',
        )

        Interested.objects.create(
            user=user1,
            event=event1
        )
        Interested.objects.create(
            user=user2,
            event=event2
        )

    def test_can_retrieve_interested_using_valid_id(self):
        response = self.client.get('/interested/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_interested_using_invalid_id(self):
        response = self.client.get('/interested/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_their_own_interested(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/interested/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_others_interested(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/interested/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cannot_be_interested_to_the_same_event_twice(self):
        self.client.login(username='user1', password='pass1')
        user1 = User.objects.get(username='user1')
        event1 = Event.objects.get(pk=1)
        response = self.client.post(
            '/interested/', {'user': user1, 'event': event1}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
