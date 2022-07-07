from django.views.generic import TemplateView, DetailView
from snippet.models import Snippet


class HomeView(TemplateView):
    template_name = 'home.html'


class SnippetView(DetailView):
    model = Snippet
    template_name = 'snippet.html'
    context_object_name = 'snippet'