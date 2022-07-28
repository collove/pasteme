from django.views.generic import DetailView, TemplateView

from snippet.models import Snippet
from pypi.models import Statistic


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stats"] = Statistic.objects.last()
        return context


class SnippetView(DetailView):
    model = Snippet
    template_name = 'snippet.html'
    context_object_name = 'snippet'