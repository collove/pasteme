from os import path

from django.conf import settings
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from .models import Snippet


class SnippetSerializer(ModelSerializer):
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['url'] = path.join(settings.DOMAIN_URL, 'paste', data['id'])
        return data

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'body', 'language']
        read_only_fields = ['id']