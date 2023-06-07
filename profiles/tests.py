from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    """
    Tests for the Profile model list view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        user2 = User.objects.create_user(username='user2', password='pass2')
        user3 = User.objects.create_user(username='user3', password='pass3')

    def test_profile_automatically_created_on_user_creation(self):
        response = self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 3)

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailViewTests(APITestCase):
    """
    Tests for the Profile model detail view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        user2 = User.objects.create_user(username='user2', password='pass2')
        user3 = User.objects.create_user(username='user3', password='pass3')

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_profile_if_logged_in(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.put(
            '/profiles/1/', {'email': 'Test@gmail.com'}
        )
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.email, 'Test@gmail.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_others_profile(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.put(
            '/profiles/2/', {'email': 'Test@gmail.com'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_profile(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_others_profile(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/profiles/3/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
