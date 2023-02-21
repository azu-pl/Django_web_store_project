from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sign-up/', views.sign_up_view, name='sign_up'),
]
