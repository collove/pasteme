from django.utils import timezone
from django.views.generic import DetailView, TemplateView

from modals.models import Modal
from pypi.models import Statistic
from snippet.models import Snippet


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stats"] = Statistic.objects.last()
        context["modal"] = Modal.objects.filter(expires_at__gte=timezone.now()).last()
        return context


class SnippetView(DetailView):
    model = Snippet
    template_name = "snippet.html"
    context_object_name = "snippet"
