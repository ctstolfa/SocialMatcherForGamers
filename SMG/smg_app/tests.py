from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()


class UserLogin(TestCase):

    def setUp(self):
        user_a = User(username="UserTest")
        user_a_pw = "TestingThisPassword1@"
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        self.assertTrue(self.user_a.check_password("TestingThisPassword1@"))
