# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal:
from .models import Event
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class EventListViewTests(APITestCase):
    """
    Tests for the Event model list view
    """

    def setUp(self):
        User.objects.create_user(username='user1', password='pass1')

    def test_can_list_events(self):
        user1 = User.objects.get(username='user1')
        Event.objects.create(owner=user1, title='test title')
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_event(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.post(
            '/events/', {'title': 'test title'}
        )
        count = Event.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannnot_create_event(self):
        response = self.client.post(
            '/events/', {'title': 'test title'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class EventDetailViewTests(APITestCase):
    """
    Tests for the event model detail view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        user2 = User.objects.create_user(username='user2', password='pass2')
        user3 = User.objects.create_user(username='user3', password='pass3')

        Event.objects.create(
            owner=user1,
            title='user1 title',
        )
        Event.objects.create(
            owner=user2,
            title='user2 title',
        )
        Event.objects.create(
            owner=user3,
            title='user3 title',
        )

    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get('/events/2/')
        self.assertEqual(response.data['title'], 'user2 title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_events_using_invalid_id(self):
        response = self.client.get('/events/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_events_if_logged_in(self):
        self.client.login(username='user2', password='pass2')
        response = self.client.put(
            '/events/2/', {'title': 'new title'}
        )
        event = Event.objects.filter(pk=2).first()
        self.assertEqual(event.title, 'new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_others_events(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.put(
            '/events/2/', {'title': 'user1 title'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_events(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/events/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_others_events(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/events/3/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
