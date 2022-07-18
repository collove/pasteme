from django.views.generic import DetailView, TemplateView

from snippet.models import Snippet


class HomeView(TemplateView):
    template_name = 'home.html'


class SnippetView(DetailView):
    model = Snippet
    template_name = 'snippet.html'
    context_object_name = 'snippet'