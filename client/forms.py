from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from .models import Client

User = get_user_model()
class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            "first_name",
            "second_name",
            "order_name",
            "total",
            "phone_number",
            "comment",
            "seamstress",
        )

class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    second_name = forms.CharField(max_length=20)
    order_name = forms.CharField(max_length=50)
    total = forms.IntegerField(min_value=0)
    phone_number = forms.CharField(max_length=16)
    comment = forms.CharField(max_length=500)


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}    