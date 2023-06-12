# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal:
from events.models import Event
from .models import Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CommentsListViewTests(APITestCase):
    """
    Tests for the Comment model list view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        event1 = Event.objects.create(
            user=user1,
            title='Test Event',
            country='Germany'
        )

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


class CommentDetailViewTests(APITestCase):
    """
    Test for Comment detail view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        user2 = User.objects.create_user(username='user2', password='pass2')
        user3 = User.objects.create_user(username='user3', password='pass3')

        event1 = Event.objects.create(
            user=user1,
            title='user1 title',
            country='Germany'
        )
        Comment.objects.create(
            user=user1,
            event=event1,
            content='User1 comment'
        )
        Comment.objects.create(
            user=user2,
            event=event1,
            content='User2 comment'
        )
        Comment.objects.create(
            user=user3,
            event=event1,
            content='User3 comment'
        )

    def test_can_retrieve_comment_using_valid_id(self):
        response = self.client.get('/comments/3/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/comments/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_comments_if_logged_in(self):
        self.client.login(username='user2', password='pass2')
        response = self.client.put(
            '/comments/2/', {'content': 'user2 new comment'}
        )
        comment = Comment.objects.filter(pk=2).first()
        self.assertEqual(comment.content, 'user2 new comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_others_comments(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.put(
            '/comments/2/', {'content': 'user1 new comment'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_comment(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/comments/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_others_comments(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/comments/3/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
