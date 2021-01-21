from django.test import SimpleTestCase
from django.urls import reverse, resolve  # new
from .views import HomePageView  # new


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)