from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterUserForm(UserCreationForm):
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


class CreateCommentForm(forms.Form):

    # creator = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL)
    # product = models.ForeignKey('Product', on_delete=models.PROTECT)
    title = forms.CharField(max_length=30)
    comment = forms.Textarea()
    score = forms.IntegerField(min_value=1, max_value=5)
