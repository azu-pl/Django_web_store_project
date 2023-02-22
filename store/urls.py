from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('sign-up/', views.sign_up_view, name='sign_up'),
    path('profile/', views.profile_view, name='profile'),
]
