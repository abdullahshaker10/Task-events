from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="abdullah", email="abdullah@email.com", password="testpass123"
        )
        self.assertEqual(user.username, "abdullah")
        self.assertEqual(user.email, "abdullah@email.com")
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"
    

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.last().username, self.username)
        self.assertEqual(get_user_model().objects.last().email, self.email)
