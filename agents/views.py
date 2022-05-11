from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import  LoginRequiredMixin
from client.models import *

# Create your views here.

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/list.html'

    def get_queryset(self):
        return Seamstress.objects.all()