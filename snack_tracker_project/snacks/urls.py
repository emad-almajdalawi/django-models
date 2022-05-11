from django.urls import path
from .views import SnackListView, HomeView

urlpattern = [
    path('',HomeView.as_view(), name='home'),
    path('snacks-list', SnackListView.as_view(), name='snacks-list'),
]