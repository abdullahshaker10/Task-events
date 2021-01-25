from django.test import Client, TestCase
from django.urls import reverse
from .models import Event
from django.contrib.auth import get_user_model
import json
from datetime import datetime


class EventsTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.owner = User.objects.create_user(
            username="abdullah", email="abdullah@email.com", password="testpass123"
        )

        self.user = User.objects.create_user(
            username="customer", email="a@email.com", password="testpass123"
        )
        self.user2 = User.objects.create_user(
            username="customer2", email="a2@email.com", password="testpass123"
        )
        self.event = Event.objects.create(
            title="event1",
            description="event1",
            date=datetime(2020, 4, 16),
            owner=self.owner,
        )
        self.event.participant.add(self.user)

    def test_create_event(self):
        self.assertEqual(f"{self.event.title}", "event1")
        self.assertEqual(f"{self.event.description}", "event1")
        self.assertEqual(f"{self.event.owner}", "abdullah")

    def test_event_list_view(self):
        response = self.client.get(reverse("events"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "event1")
        self.assertTemplateUsed(response, "events/events_list.html")

    def test_event_detail_view(self):
        response = self.client.get(self.event.get_absolute_url())
        no_response = self.client.get("/event/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "event1")
        self.assertTemplateUsed(response, "events/event_detail.html")

    def test_add_participant(self):
        self.client.force_login(self.user2)
        response = self.client.patch(
            reverse("add_participant", kwargs={"pk": self.event.id}),
            data=json.dumps({"id": None}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(self.event.participant.all()), [self.user, self.user2])

    def test_withdraw_event(self):
        self.client.force_login(self.user2)
        response = self.client.patch(
            reverse("withdraw_event", kwargs={"pk": self.user2.id}),
            data=json.dumps({"id": self.event.id}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(self.event.participant.all()), [self.user])
