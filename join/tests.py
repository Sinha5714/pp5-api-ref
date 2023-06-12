from django.contrib.auth.models import User
from events.models import Event
from .models import Join
from rest_framework import status
from rest_framework.test import APITestCase


class JoinListViewTests(APITestCase):
    """
    Tests for the Join list view
    """

    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='pass1')
        event1 = Event.objects.create(
            user=user1,
            title='event',
            country='Germany'
        )

    def test_can_list_join_requests(self):
        user1 = User.objects.get(username='user1')
        event1 = Event.objects.get(pk=1)
        Join.objects.create(
            user=user1,
            event=event1,
            email='Test@gmail.com',
            reason='Test reason'
        )
        response = self.client.get('/join/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cannot_create_join_request_for_an_event(self):
        event1 = Event.objects.get(pk=1)
        response = self.client.post(
            '/join/', {
                'event': 1,
                'reason': 'Test reason'
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
            user=user1,
            title='User1 title',
            country='Germany'
        )
        event2 = Event.objects.create(
            user=user2,
            title='User2 title',
            country='Sweden'
        )

        Join.objects.create(
            user=user1,
            event=event1,
            email='Test@gmail.com',
            reason='Test reason'
        )
        Join.objects.create(
            user=user2,
            event=event2,
            email='Test2@gmail.com',
            reason='Test2 reason'
        )

    def test_can_retrieve_join_request_using_valid_id(self):
        response = self.client.get('/join/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_join_request_using_invalid_id(self):
        response = self.client.get('/join/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_own_join_request(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.put(
            '/join/1/', {'reason': 'New reason'}
        )
        join = Join.objects.filter(pk=1).first()
        self.assertEqual(join.reason, 'New reason')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_someone_elses_join_request(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.put(
            '/join/2/', {'reason': 'User1 reason'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_own_join_request(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/join/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_others_join_request(self):
        self.client.login(username='user1', password='pass1')
        response = self.client.delete('/join/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cannot_send_join_request_to_the_same_event_twice(self):
        self.client.login(username='user1', password='pass1')
        user1 = User.objects.get(username='user1')
        event1 = Event.objects.get(pk=1)
        response = self.client.post(
            '/join/', {'user': user1, 'event': event1}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
