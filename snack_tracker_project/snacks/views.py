from django.shortcuts import render
from django.views.generic import TemplateView, ListView

class HomeView(TemplateView):
    template_name = ''

class SnackListView(ListView):
    template_name = 'snack_list.html'

