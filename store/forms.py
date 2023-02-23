from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ResisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        labels = {'username': "Nazwa", 'password': "hasło", 'first_name': "Imię", 'last_name': "Nazwisko"}

class CreateUserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ['user',]

