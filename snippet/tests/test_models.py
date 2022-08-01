from django.test import TestCase

from snippet.constants import LANGUAGES
from snippet.models import Snippet


class SnippetTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.sample = {
            "title": "sample title",
            "body": "code snippet",
            "language": LANGUAGES[0][1],
        }

    def setUp(self) -> None:
        self.snippet = Snippet.objects.create(**self.sample)

    def test_if_obj_returns_same_fields(self):
        fields = {
            "title": self.snippet.title,
            "body": self.snippet.body,
            "language": self.snippet.language,
        }
        self.assertEqual(fields, self.sample)

    def test_if_obj_is_retrievable(self):
        self.assertIsInstance(Snippet.objects.get(id=self.snippet.id), Snippet)

    def test_sid_length(self):
        self.assertEqual(len(self.snippet.id), 5)
