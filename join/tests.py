# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal:
from events.models import Event
from .models import Join
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class JoinListViewTests(APITestCase):
    """
    Tests for the Join list view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        event1 = Event.objects.create(
            owner=user1,
            title='event',
        )

    def test_can_list_join_request(self):
        user1 = User.objects.get(username='user1')
        event1 = Event.objects.get(pk=1)
        Join.objects.create(
            owner=user1,
            event=event1,
        )
        response = self.client.get('/join/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_join_request_for_an_event(self):
        self.client.login(username='user1', password='pass1')
        event1 = Event.objects.get(pk=1)
        user1 = User.objects.get(username='user1')
        response = self.client.post(
            '/join/', {
                'owner': user1,
                'event': 1,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_join_request_for_an_event(self):
        event1 = Event.objects.get(pk=1)
        response = self.client.post(
            '/join/', {
                'event': 1,
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class JoinDetailViewTests(APITestCase):
    """
    Test for Join detail view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        user2 = User.objects.create_user(username='user2', password='pass2')

        event1 = Event.objects.create(
            owner=user1,
            title='User1 title',
        )
        event2 = Event.objects.create(
            owner=user2,
            title='User2 title',
        )

        Join.objects.create(
            owner=user1,
            event=event1,
        )
        Join.objects.create(
            owner=user2,
            event=event2,
        )

    def test_can_retrieve_join_request_using_valid_id(self):
        response = self.client.get('/join/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_join_request_using_invalid_id(self):
        response = self.client.get('/join/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_delete_their_own_join_request(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/join/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_others_join_request(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/join/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cannot_be_able_to_send_join_to_the_same_event_twice(self):
        self.client.login(username='user1', password='pass1')
        user1 = User.objects.get(username='user1')
        event1 = Event.objects.get(pk=1)
        response = self.client.post(
            '/join/', {'owner': user1, 'event': event1}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
