from django.test import Client, TestCase
from django.urls import reverse


class SnippetTemplateTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
