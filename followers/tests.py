from django.contrib.auth.models import User
from .models import Follower
from rest_framework import status
from rest_framework.test import APITestCase


class FollowerListViewTests(APITestCase):
    """
    Test for Follower List View
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        user2 = User.objects.create_user(username='user2', password='pass2')
        user3 = User.objects.create_user(username='user3', password='pass3')

        Follower.objects.create(
            user=user1,
            followed=user2
        )
        Follower.objects.create(
            user=user1,
            followed=user3
        )

    def test_can_list_follower(self):
        user1 = User.objects.get(username='user1')
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_follow(self):
        """
        user2 want to follow user3
        """
        self.client.login(username='user2', password='pass2')
        response = self.client.post(
            '/followers/', {
                'user': 2,
                'followed': 3
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_follow(self):
        user1 = User.objects.get(username='user1')
        user2 = User.objects.get(username='user2')
        response = self.client.post(
            '/followers/', {
                'user': user1,
                'followed': user2
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_cannot_follow_someone_they_already_follow(self):
        """
        user1 trying to follow user3 again
        """
        self.client.login(username='user1', password='pass1')
        response = self.client.post(
            '/followers/', {'owner': 1, 'followed': 3}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
