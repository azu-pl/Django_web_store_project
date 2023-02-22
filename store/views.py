from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib.auth import login, logout, authenticate
from store.models import Profile, Category
from django.contrib.auth.models import User


def store(request):
    context = {}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def sign_up_view(request):
    if request.method == 'POST':
        form = forms.ResisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store')

    else:
        form = forms.ResisterUserForm()

    return render(request, 'registration/sign_up.html', {'form': form})

def profile_view(request):
    # user = Profile.objects.get(phone_number='')
    # print(user.name)
    profile = get_object_or_404(Profile, id=1)
    context = {'profile': profile}
    return render(request, 'store/profile.html', context)

