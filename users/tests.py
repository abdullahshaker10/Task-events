from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from events.models import Event
from datetime import datetime


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
        self.assertEqual(
            get_user_model().objects.last().username, self.username)
        self.assertEqual(get_user_model().objects.last().email, self.email)


class MyEventsTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.owner = User.objects.create_user(
            username="abdullah", email="abdullah@email.com", password="testpass123"
        )
        self.event = Event.objects.create(
            title="event1",
            description="event1",
            date=datetime(2020, 4, 16),
            owner=self.owner,
        )
        self.user = User.objects.create_user(
            username="customer", email="a@email.com", password="testpass123"
        )
        self.event.participant.add(self.user)

    def test_my_events_list(self):
        self.client.force_login(self.owner)
        response = self.client.get(reverse("my_events"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "event1")
        self.assertTemplateUsed(response, "events/my_events_list.html")

    def test_subscribed_event_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("subscribed_events"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "event1")
        self.assertTemplateUsed(response, "events/subscribed_events_list.html")
