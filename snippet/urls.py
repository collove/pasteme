from django.urls import path
from .views import api, template

urlpatterns = [
    path('', template.HomeView.as_view(), name='home'),
    path('paste/<str:pk>/', template.SnippetView.as_view(), name='view_paste'),

    path('api/v1/create-paste/', api.CreateSnippetAPI.as_view(), name='create_paste'),
    path('api/v1/get-paste/<str:pk>/', api.GetSnippetAPI.as_view(), name='get_paste'),
]