from django.contrib.auth import get_user_model
from .models import Account
from django.test import TestCase
User = get_user_model()


class UserLogin(TestCase):

    def setUp(self):
        user_a = User(username='UserTest')
        user_a_pw = 'TestingThisPassword1@'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        self.user_a = user_a

        account_a = Account('UserTest')
        account_a.time = ('Morning', 'Midnight')
        account_a.role = 1
        account_a.days = 'Wednesday'
        account_a.gameStyle = 'Competitive'
        account_a.genres = ('RPG', 'Horror', 'Survival')
        self.account_a = account_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        self.assertTrue(self.user_a.check_password("TestingThisPassword1@"))

    def test_account_exists(self):
        account_count = User.objects.all().count()
        self.assertEqual(account_count, 1)
        self.assertNotEqual(account_count, 0)

    def test_account_attributes(self):
        self.assertEqual(self.account_a.time, ('Morning', 'Midnight'))
        self.assertEqual(self.account_a.role, 1)
        self.assertEqual(self.account_a.days, 'Wednesday')
        self.assertEqual(self.account_a.gameStyle, 'Competitive')
        self.assertEqual(self.account_a.genres, ('RPG', 'Horror', 'Survival'))