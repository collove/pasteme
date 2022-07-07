from rest_framework.generics import RetrieveAPIView, CreateAPIView
from snippet.serializers import SnippetSerializer
from snippet.models import Snippet


class CreateSnippetAPI(CreateAPIView):
    model = Snippet
    serializer_class = SnippetSerializer


class GetSnippetAPI(RetrieveAPIView):
    model = Snippet
    lookup_field = 'pk'
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()