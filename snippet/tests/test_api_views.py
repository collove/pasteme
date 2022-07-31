import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from snippet.constants import LANGUAGES
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer


class SnippetAPITestCase(APITestCase):
    def setUp(self):
        self.sample = {
            "title": "sample title",
            "body": "code snippet",
            "language": LANGUAGES[0][0],
        }

    def test_create_snippet(self):
        url = reverse("create-paste")
        response = self.client.post(
            url, json.dumps(self.sample), content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 1)
        self.assertEqual(Snippet.objects.get().title, "sample title")

    def test_if_object_exists(self):
        post_response = self.client.post(
            reverse("create-paste"),
            json.dumps(self.sample),
            content_type="application/json",
        )

        id = post_response.json()["id"]

        get_response = self.client.get(
            reverse("get-paste", args=[id]), content_type="application/json"
        )

        get_serialized = SnippetSerializer(get_response.json()).data

        self.assertEqual(post_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_serialized, post_response.json())
