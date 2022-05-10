from multiprocessing import context
from multiprocessing.connection import Client
from re import template
from turtle import update
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import *
import client

# Create your views here.

class HomeView(TemplateView):
    template_name = "main.html"

class ListsView(ListView):
    template_name = "clients_list.html"
    queryset = models.Client.objects.all()
    context_object_name = "clients"

class ClientDetailsView(DetailView):
    template_name = "details.html"
    queryset = models.Client.objects.all()
    context_object_name = "client"

def table(request):
    client = models.Client.objects.all()
    context = {
        "clients": client
    }       
    return render(request, "table.html", context)
   
class CliendCreateView(CreateView):
    template_name = "clients/create.html"
    form_class = ClientModelForm

    def get_success_url(self):
        return reverse("client:clients-list")



class ClientUpdateView(UpdateView):
    template_name = "clients/update.html"
    form_class = ClientModelForm
    queryset = models.Client.objects.all()

    def get_success_url(self):
        return reverse("client:clients-list")


class ClientDeleteView(DeleteView):
    template_name = "clients/delete.html"
    form_class = ClientModelForm
    queryset = models.Client.objects.all()

    def get_success_url(self):
        return reverse("client:clients-list")
    

    
