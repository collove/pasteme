from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="PasteMe API Documentation",
        default_version="v1",
        description="API endpoints for PasteMe RESTful service.",
        contact=openapi.Contact(email="lnxpylnxpy@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=None,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "apidocs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path(
        "disclaimer/",
        TemplateView.as_view(
            template_name="disclaimer.html",
            extra_context={"SITE_URL": settings.SITE_URL},
        ),
        name="disclaimer",
    ),
    path("blog/", include("blog.urls")),
    path("", include("snippet.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
