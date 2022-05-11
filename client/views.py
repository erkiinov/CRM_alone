from multiprocessing import context
from multiprocessing.connection import Client
from re import template
from turtle import update
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Client
from django.db.models import Q

# Create your views here.


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = NewUserForm

    def get_success_url(self):
        return reverse("client:clients-list")

class HomeView(TemplateView):
    template_name = "main.html"

class ListsView(LoginRequiredMixin, ListView):
    template_name = "clients/clients_list.html"
    queryset = models.Client.objects.all()
    context_object_name = "clients"

class ClientDetailsView(LoginRequiredMixin, DetailView):
    template_name = "details.html"
    queryset = models.Client.objects.all()
    context_object_name = "client"

   
class CliendCreateView(LoginRequiredMixin, CreateView):
    template_name = "clients/create.html"
    form_class = ClientModelForm

    def get_success_url(self):
        return reverse("client:clients-list")



class ClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "clients/update.html"
    form_class = ClientModelForm
    queryset = models.Client.objects.all()

    def get_success_url(self):
        return reverse("client:clients-list")


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "clients/delete.html"
    form_class = ClientModelForm
    queryset = models.Client.objects.all()
    context_object_name = "client"

    def get_success_url(self):
        return reverse("client:clients-list")
    

def home(request) :
    if 'q' in request.GET:
        searching_word = request.GET['q']
        Full = Q(Q(first_name__icontains=searching_word) | Q(second_name__icontains=searching_word) | Q(order_name__icontains=searching_word))
        Clients = Client.objects.filter(Full)
    else:
        Clients = Client.objects.all()

    context = {
        'Client': Clients
    }
    return render(request, 'clients/clients_list.html', context)  
