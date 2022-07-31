from django.views.generic import DetailView, ListView

from blog.models import Blog


class BlogListView(ListView):
    template_name = 'blogs.html'
    queryset = Blog.objects.all()
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'