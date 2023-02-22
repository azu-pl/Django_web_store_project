from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ResisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'address']
        labels = {'username': "Nazwa", 'password': "hasło", 'first_name': "Imię", 'last_name': "Nazwisko", 'address': "adres"}
