from django.contrib import admin
from django.urls import path, include
from client.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('clients/', include('client.urls', namespace="client"))
]
