from django.urls import path
from . import views
from .views import ProfileCreateView

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('products/', views.products_list_view, name='products_list'),
    path('products/<int:id>/', views.products_detail, name='products_detail'),
    path('categories/', views.categories_list_view, name='categories_list'),
    path('subcategories/', views.subcategories_list_view, name='subcategories_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('sign-up/', views.sign_up_view, name='sign_up'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile_create')
]
