from rest_framework.generics import CreateAPIView, RetrieveAPIView

from snippet.models import Snippet
from snippet.serializers import SnippetSerializer


class CreateSnippetAPI(CreateAPIView):
    model = Snippet
    serializer_class = SnippetSerializer


class GetSnippetAPI(RetrieveAPIView):
    model = Snippet
    lookup_field = "pk"
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
