from django.urls import path
from . import views
from .views import ProfileCreateView, HelloView, ProfileView, StoreMainView, CartView, ProductDetailView, SignUp, \
    CheckoutView, CategoryDetailView, SubcategoryDetailView, CommentCreateView

urlpatterns = [
    # path('', views.store, name='store'),
    path('', StoreMainView.as_view(), name='store'),
    # path('hello/', HelloView.as_view()),
    # path('cart/', views.cart, name='cart'),
    path('cart/', CartView.as_view(), name='cart'),
    # path('products/', views.products_list_view, name='products_list'),
    # path('products/<int:id>/', views.products_detail, name='products_detail'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    # path('categories/', views.categories_list_view, name='categories_list'),
    # path('categories/<int:id>/', views.categories_detail_view, name='categories_detail_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='categories_detail_list'),
    path('subcategories/', views.subcategories_list_view, name='subcategories_list'),
    # path('subcategories/<int:id>/', views.subcategories_detail_view, name='subcategories_detail_list'),
    path('subcategories/<int:pk>/', SubcategoryDetailView.as_view(), name='subcategories_detail_list'),
    # path('checkout/', views.checkout, name='checkout'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('sign-up/', views.sign_up_view, name='sign_up'),
    path('sign-up/', SignUp.as_view(), name='sign_up'),
    # path('profile/', views.profile_view, name='profile'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile_create'),
    path('comment/', CommentCreateView.as_view()),
]
