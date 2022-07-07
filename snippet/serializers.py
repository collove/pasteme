from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Snippet


class SnippetSerializer(ModelSerializer):
    
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'body', 'language']
        read_only_fields = ['id']