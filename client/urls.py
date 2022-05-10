from html.entities import html5


from django.urls import path
from .views import *
app_name = "client"

urlpatterns = [
    path('', ListsView.as_view(), name="clients-list"),
    path('info=<int:pk>/', ClientDetailsView.as_view(), name="user-info"),
    path('update-user=<int:pk>/', ClientUpdateView.as_view(), name="update-user"),
    path('delete-user=<int:pk>/', ClientDeleteView.as_view(), name="delete-user"),
    path('create-client/', CliendCreateView.as_view(), name="client-create"),
    path('clients-table/', table, name="table"),
]

