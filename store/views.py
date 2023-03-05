from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from django.contrib.auth import login, logout, authenticate
from store.models import Profile, Category, Product, Subcategory, Comment, OrderItem, Order
from django.contrib.auth.models import User
from store.forms import CreateUserProfileForm, RegisterUserForm, CreateCommentForm, ProfileUpdateForm, UserUpdateForm
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.db.models import Q
import json


class BaseStoreView(TemplateView):
    template_name = "store/base.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            order, created = Order.objects.get_or_create(profile=profile, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']

        context['categories'] = Category.objects.all()
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems

        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class BaseDetailView(DetailView):
    template_name = "store/base.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            order, created = Order.objects.get_or_create(profile=profile, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']

        context['categories'] = Category.objects.all()
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems

        return context


class BaseCreateView(CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class StoreMainView(BaseStoreView):
    template_name = 'store/store.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = Product.objects.all()
    #     return context

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            order, created = Order.objects.get_or_create(profile=profile, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']

        context['products'] = Product.objects.all()
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems

        return context

# def store(request):
#     products = Product.objects.all()
#     ctx = {'products': products}
#     return render(request, 'store/store.html', ctx)


class CartView(BaseStoreView):
    template_name = 'store/cart.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            order, created = Order.objects.get_or_create(profile=profile, complete=False)
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cartItems = order['get_cart_items']

        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems

        return context


class CheckoutView(BaseStoreView):
    template_name = 'store/checkout.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            profile = self.request.user.profile
            order, created = Order.objects.get_or_create(profile=profile, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}

        context['items'] = items
        context['order'] = order

        return context


def updateItem(request):
    # data = json.loads(request.data)
    data = json.loads(request.body.decode("utf-8"))
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)

    profile = request.user.profile
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(profile=profile, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Produkt dodany do koszyka!', safe=False)


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


class SignUp(BaseCreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('store')
    template_name = 'registration/sign_up.html'


# def sign_up_view(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('store')
#
#     else:
#         form = RegisterUserForm()
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
    template_name = 'store/profile.html'
    form_class = CreateUserProfileForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # here we set default logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, BaseCreateView):
    model = Comment
    form_class = CreateCommentForm
    # fields = '__all__'
    template_name = 'store/add_comment.html'

    def get_success_url(self):
        return reverse('products_detail', kwargs={'pk': self.object.product.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel'] = reverse('products_detail', kwargs={'pk': self.kwargs['pk']})
        return context

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        form.instance.creator_id = self.request.user.pk
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CreateCommentForm
    # fields = ['title', 'comment', 'score']
    template_name = 'store/add_comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cancel'] = self.request.META.get('HTTP_REFERER')
        return context

    def get_success_url(self):
        return reverse('profile')


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('profile')
    template_name = 'store/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cancel'] = self.request.META.get('HTTP_REFERER')
        return context


class CommentProductUpdateView(CommentUpdateView):
    
    def get_success_url(self):
        return reverse('products_detail', kwargs={'pk': self.object.product.pk})


class CommentProductDeleteView(CommentDeleteView):

    def get_success_url(self):
        return reverse('products_detail', kwargs={'pk': self.object.product.pk})


# class UserUpdateProfileView(LoginRequiredMixin, UpdateView):
#     template_name = 'store/profile.html'
#     context_object_name = 'user'
#     queryset = Profile.objects.all()
#     form_class = ProfileUpdateForm
#     success_url = reverse_lazy('profile')
#
#     def get_context_data(self, **kwargs):
#         context = super(UserUpdateProfileView, self).get_context_data(**kwargs)
#         user = self.request.user
#         context['profile_form'] = ProfileUpdateForm(instance=self.request.user.pk,
#                                                     initial={'first_name': user.first_name, 'last_name': user.last_name,
#                                                              'email': user.email})
#         return context
#
#     def form_valid(self, form):
#         profile = form.save(commit=False)
#         user = profile.user
#         user.last_name = form.cleaned_data['last_name']
#         user.first_name = form.cleaned_data['first_name']
#         user.email = form.cleaned_data['email']
#         user.save()
#         profile.save()
#         # return HttpResponseRedirect(reverse('profile', kwargs={'pk': self.get_object().id}))
#         return super().form_valid(form)

def user_update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'categories': Category.objects.all(),
        'cancel': request.META.get('HTTP_REFERER')
    }

    return render(request, 'store/profile_update.html', context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
        'categories': Category.objects.all(),
        'cancel': request.META.get('HTTP_REFERER')
    }

    return render(request, 'store/user_update.html', context)


class UserPasswordChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cancel'] = self.request.META.get('HTTP_REFERER')
        return context


class UserDeleteView(LoginRequiredMixin, CommentDeleteView):
    model = User
    success_url = reverse_lazy('store')
    template_name = 'store/confirm_delete.html'

    def dispatch(self, request, *args, **kwargs):
        print(kwargs)
        if not request.user.is_authenticated or request.user.pk != self.kwargs['pk']:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


# class SearchStoreList(ListView):
#     model = Product
#     template_name = 'store/store.html'
#
#     def get_queryset(self):
#         q_s = self.request.GET.get('q_s')
#         if q_s:
#             object_list = self.model.objects.filter(name__icontains=q_s)
#         else:
#             object_list = self.model.objects.all()
#         return object_list.order_by('-name')

def search_product(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

        context = {
            'searched': searched,
            'products': products,
            'categories': Category.objects.all(),
        }

        return render(request, 'store/search_product.html', context)

    else:
        return render(request, 'store/store.html')
