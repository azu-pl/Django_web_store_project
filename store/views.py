from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View

from . import forms
from django.contrib.auth import login, logout, authenticate
from store.models import Profile, Category, Product, Subcategory
from django.contrib.auth.models import User
from store.forms import CreateUserProfileForm
from django.views.generic import CreateView, TemplateView, DetailView
from django.urls import reverse_lazy, reverse


class BaseStoreView(TemplateView):
    template_name = "store/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BaseDetailView(DetailView):
    template_name = "store/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BaseCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class StoreMainView(BaseStoreView):
    template_name = 'store/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


# def store(request):
#     products = Product.objects.all()
#     ctx = {'products': products}
#     return render(request, 'store/store.html', ctx)

class CartView(BaseStoreView):
    template_name = 'store/cart.html'

# def cart(request):
#     context = {}
#     return render(request, 'store/cart.html', context)


# def products_list_view(request):
#     products = Product.objects.all()
#     ctx = {'products': products}
#     return render(request, 'store/products_list_1.html', ctx)

class ProductDetailView(BaseDetailView):
    template_name = "store/product_detail.html"
    model = Product


# class ProductDetailView(BaseStoreView):
#     template_name = "store/product_detail.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             product = Product.objects.get(pk=kwargs['pk'])
#         except Product.DoesNotExist:
#             raise Http404("Product does not exist")
#
#         context['product'] = product
#         return context

# def products_detail(request, id):
#     product = get_object_or_404(Product, id=id)
#     ctx = {'product': product}
#     return render(request, 'store/products_detail.html', ctx)


# def categories_list_view(request):
#     #categories = Category.objects.all()
#     #ctx = {'categories': categories}
#     pass

class CategoryDetailView(BaseStoreView):
    template_name = "store/store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(subcategory__category=kwargs['pk'])
        print(context)
        return context


class SubcategoryDetailView(BaseStoreView):
    template_name = "store/store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(subcategory_id=kwargs['pk'])
        return context
def categories_detail_view(request, id):
    pass


def subcategories_detail_view(request, id):
    pass


def subcategories_list_view(request):
    pass


class CheckoutView(BaseStoreView):
    template_name = 'store/checkout.html'


class SignUp(BaseCreateView):
    form_class = forms.ResisterUserForm
    success_url = reverse_lazy('store')
    template_name = 'registration/sign_up.html'


# def sign_up_view(request):
#     if request.method == 'POST':
#         form = forms.ResisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('store')
#
#     else:
#         form = forms.ResisterUserForm()
#
#     return render(request, 'registration/sign_up.html', {'form': form})

# def profile_view(request):
#     # profile = get_object_or_404(Profile, user_id=request.user.pk)
#     try:
#         profile = Profile.objects.get(user_id=request.user.pk)
#     except Profile.DoesNotExist:
#         return redirect('profile_create')
#     context = {'profile': profile}
#     return render(request, 'store/profile.html', context)


class HelloView(BaseStoreView):
    template_name = "store/hello.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "John"
        return context


class ProfileView(BaseStoreView):
    template_name = "store/profile.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # try:
    #     #     profile = Profile.objects.get(user_id=self.request.user.pk)
    #     #
    #     # except Profile.DoesNotExist:
    #     #     return redirect('profile_create')
    #
    #     # context['profile'] = profile
    #     print(context)
    #     return context

    def get(self, request, *args, **kwargs):
        # self.object = self.get_object()
        context = self.get_context_data(**kwargs)
        try:
            profile = Profile.objects.get(user_id=self.request.user.pk)
            context['profile'] = profile
            return self.render_to_response(context)
        except:
            return HttpResponseRedirect(reverse("profile_create"))


class ProfileCreateView(BaseCreateView):
    template_name = 'store/form.html'
    form_class = CreateUserProfileForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # here we set default logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)


