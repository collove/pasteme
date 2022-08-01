from django.contrib import admin
from django.urls import include, path
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
   # path('admin/', admin.site.urls),
   path('apidocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('blog/', include('blog.urls')),
   path('', include('snippet.urls')),
]
