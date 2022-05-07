from multiprocessing import context
from multiprocessing.connection import Client
from re import template
from turtle import update
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
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
   

def create_client(request):
    forms = ClientModelForm()
    if request.method == "POST":
        form = ClientModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/clients/')

    context = {
        'forms': forms,
    }
    return render(request, "html.html", context)

def client_update(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientModelForm(instance=client)
    if request.method == "POST":
        form = ClientModelForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("/clients")  
    context = {
        'form':form,
        'client':client
    }
    return render(request, 'update.html', context)

def client_delete(request, pk):
    client = Client.objects.get(id=pk)
    client.delete()
    return redirect("/clients/")