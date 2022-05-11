from django.contrib import admin
from django.urls import path, include
from client.views import HomeView, SignupView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('clients/', include('client.urls', namespace="client")),
    path('log-in/', LoginView.as_view(), name="login"),
    path('log-out/', LogoutView.as_view(), name="logout"),
    path('sign-up/', SignupView.as_view(), name="signup"),
]
