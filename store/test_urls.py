from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import StoreMainView, CartView, CheckoutView, SignUp, ProfileView, ProfileCreateView, user_update_profile
from store.views import UserPasswordChangeView, ProductDetailView, CategoryDetailView
from store.views import subcategories_list_view, subcategories_detail_view


class TestUrls(SimpleTestCase):

    def test_store_resolved(self):
        url = reverse('store')
        self.assertEqual(resolve(url).func.view_class, StoreMainView)

    def test_cart_resolved(self):
        url = reverse('cart')
        self.assertEqual(resolve(url).func.view_class, CartView)

    def test_checkout_resolved(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func.view_class, CheckoutView)

    def test_signup_resolved(self):
        url = reverse('sign_up')
        self.assertEqual(resolve(url).func.view_class, SignUp)

    def test_profile_resolved(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func.view_class, ProfileView)

    def test_profile_create_resolved(self):
        url = reverse('profile_create')
        self.assertEqual(resolve(url).func.view_class, ProfileCreateView)

    def test_update_profile_resolved(self):
        url = reverse('update_profile')
        self.assertEqual(resolve(url).func, user_update_profile)

    def test_change_password_resolved(self):
        url = reverse('change_password')
        self.assertEqual(resolve(url).func.view_class, UserPasswordChangeView)

    def test_products_detail_resolved(self):
        url = reverse('products_detail', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, ProductDetailView)

    def test_categories_detail_list_resolved(self):
        url = reverse('categories_detail_list', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, CategoryDetailView)

#