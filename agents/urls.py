from django.urls import URLPattern, path
from .views import *

app_name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name="AgentList")
]