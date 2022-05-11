from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

class HomeView(TemplateView):
    template_name = 'home.html'


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snack_object'

    # def get_queryset(self):
    #     return models.Snack.objects.all()

class SnackDeatailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack



