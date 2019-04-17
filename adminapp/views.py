from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from mainapp.models import ProductCategory
from authapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context

    def dispatch(self, request, *args, **kwargs):
        super(ProductCategoryListView, self).dispatch(self, request, *args, **kwargs)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание категории'
        return context


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Изменение категории'
        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Удаление категории'
        return context


class ShopUserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'


class ShopUserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:categories')


class ShopUserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:categories')


class ShopUserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin_custom:categories')

# Create your views here.
