from django.urls import path
from .views import SnackListView, HomeView, SnackDeatailView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('snacks-list/', SnackListView.as_view(), name='snacks_list'),
    path('snack-details/<int:pk>', SnackDeatailView.as_view(), name='snack_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)