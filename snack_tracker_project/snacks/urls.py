from django.urls import path
from .views import SnackListView, HomeView, SnackDeatailView
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('snacks-list/', SnackListView.as_view(), name='snacks_list'),
    path('snack-details/<int:pk>', SnackDeatailView.as_view(), name='snack_details')
]