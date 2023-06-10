from django.contrib.auth.models import User
from events.models import Event
from .models import Comment
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from events.models import Event
from .models import Comment
from rest_framework import status
from rest_framework.test import APITestCase


class CommentsListViewTests(APITestCase):
    """
    Tests for the Comment model list view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        event1 = Event.objects.create(user=user1, title='Test Event')

    def test_can_list_comments(self):
        user1 = User.objects.get(username='user1')
        event1 = Event.objects.get(pk=1)
        Comment.objects.create(
            user=user1,
            event=event1,
            content='Test Comment'
        )
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_comment_for_an_event(self):
        self.client.login(username='user1', password='pass1')
        event1 = Event.objects.get(pk=1)
        user1 = User.objects.get(username='user1')
        response = self.client.post(
            '/comments/', {
                'user': user1,
                'event': 1,
                'content': 'A Test Comment'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_comment_for_an_event(self):
        event1 = Event.objects.get(pk=1)
        response = self.client.post(
            '/comments/', {
                'event': 1,
                'content': 'A Test Comment'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
