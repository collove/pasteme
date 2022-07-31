from os import path

from django.conf import settings
from rest_framework.serializers import ModelSerializer

from .models import Snippet


class SnippetSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["url"] = path.join(settings.DOMAIN_URL, "paste", data["id"])
        data["theme"] = instance.get_theme_display()
        return data

    class Meta:
        model = Snippet
        fields = ["id", "title", "body", "language", "theme"]
        read_only_fields = ["id"]
