from django.contrib.auth.models import User
from ..models import Friend
from django.test import TestCase, Client
from django.urls import reverse


class FriendModelTests(TestCase):
	def setUp(self):
		self.user1 = User.objects.create_user(username='user1', password='TestingThisPassword1@')
		self.user2 = User.objects.create_user(username='user2', password='TestingThisPassword2@')
		self.friend1 = Friend.objects.create(current_user=User.objects.get(id=1))
		self.friend2 = Friend.objects.create(current_user=User.objects.get(id=2))

	def test_created_friends(self):
		self.assertEqual(self.friend1.current_user, self.user1)
		self.assertEqual(self.friend2.current_user, self.user2)

	def test_add_friend(self):
		Friend.add_friend(self.user1, self.user2)
		self.assertTrue(self.user2 in list(self.friend1.users.all()))
		self.assertFalse(self.user1 in list(self.friend2.users.all()))
		Friend.add_friend(self.user2, self.user1)
		self.assertTrue(self.user1 in list(self.friend2.users.all()))

	def test_remove_friend(self):
		Friend.add_friend(self.user1, self.user2)
		Friend.add_friend(self.user2, self.user1)
		Friend.remove_friend(self.user1, self.user2)
		self.assertFalse(self.user2 in list(self.friend1.users.all()))
		self.assertTrue(self.user1 in list(self.friend2.users.all()))
		Friend.remove_friend(self.user2, self.user1)
		self.assertFalse(self.user1 in list(self.friend2.users.all()))


class ChangeFriendViewTests(TestCase):
	def setUp(self):
		self.user1 = User.objects.create_user(username='user1', password='TestingThisPassword1@')
		self.client = Client()

	def test_add_friend(self):
		response = self.client.get(reverse('change_friend', kwargs={'operation': 'add', 'username': self.user1.username}))
		self.assertEqual(response.status_code, 302)

	def test_remove_friend(self):
		response = self.client.get(reverse('change_friend', kwargs={'operation': 'remove', 'username': self.user1.username}))
		self.assertEqual(response.status_code, 302)


class FriendRequestViewTests(TestCase):
	def setUp(self):
		self.user1 = User.objects.create_user(username='user1', password='TestingThisPassword1@')
		self.client = Client()

	def test_send_friend_req(self):
		response = self.client.get(
			reverse('friend_request', kwargs={'username': self.user1.username}))
		self.assertEqual(response.status_code, 302)

	def test_remove_friend_req_sender(self):
		response = self.client.get(
			reverse('change_friend', kwargs={'operation': 'Sender_deleting', 'username': self.user1.username}))
		self.assertEqual(response.status_code, 302)

	def test_remove_friend_req_receiver(self):
		response = self.client.get(
			reverse('change_friend', kwargs={'operation': 'Receiver_deleting', 'username': self.user1.username}))
		self.assertEqual(response.status_code, 302)
