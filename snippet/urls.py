from django.urls import path

from .views import api, template

urlpatterns = [
    path("", template.HomeView.as_view(), name="home"),
    path("paste/<str:pk>/", template.SnippetView.as_view(), name="view-paste"),
    path("api/v1/paste/", api.CreateSnippetAPI.as_view(), name="create-paste"),
    path("api/v1/paste/<str:pk>/", api.GetSnippetAPI.as_view(), name="get-paste"),
]
