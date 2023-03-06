from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile, Comment


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
        labels = {'street': "Ulica", 'number': "Numer", 'post_code': "Kod pocztowy", 'city': "Miejscowość",
                  'phone_number': "Telefon", 'info': "Informacje"}


# class CreateCommentForm(forms.Form):
#
#     # creator = models.ForeignKey('Profile', null=True, on_delete=models.SET_NULL)
#     # product = models.ForeignKey('Product', on_delete=models.PROTECT)
#     title = forms.CharField(max_length=30)
#     comment = forms.Textarea()


class CreateCommentForm(forms.ModelForm):
    score = forms.IntegerField(min_value=1, max_value=5, label="Ocena")

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['creator', 'product',]
        # widgets = {'score': forms.IntegerField(min_value=1, max_value=5),}
        labels = {'title': "Tytuł", 'comment': "Treść"}

    # def clean_score(self):
    #     submitted_score = self.cleaned_data['score']
    #     if not (1 <= submitted_score <= 5):
    #         ValidationError(
    #             "Niepoprawna wartość oceny."
    #         )

    # def clean(self):
    #     cleand_data = super().clean()
    #     # if cleand_data['score'] == 3:
    #
    #     raise ValidationError(
    #             "Niepoprawna wartość oceny."
    #         )


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # exclude = ['password1', 'password2', 'password']


class ProfileUpdateForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=32)
    # last_name = forms.CharField(max_length=32)
    # email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ['street', 'number', 'post_code', 'city',
                  'phone_number', 'info']