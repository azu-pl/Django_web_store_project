from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import login, logout, authenticate


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
            return redirect('home')

    else:
        form = forms.ResisterUserForm()

    return render(request, 'registration/sign_up.html', {'form': form})
