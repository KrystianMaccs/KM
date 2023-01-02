from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.portfolio.models import Category

class CategoryListView(ListView):
    model = Category
    template_name = 'categories/list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/create.html'
    fields = ['name']
    success_url = reverse_lazy('categories:list')

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'categories/update.html'
    fields = ['name']
    success_url = reverse_lazy('categories:list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/delete.html'
    success_url = reverse_lazy('categories:list')
