from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from apps.portfolio.models import Category, Portfolio

class CategoryListView(ListView):
    model = Category
    template_name = 'portfolio/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'portfolio/category_detail.html'
    context_object_name = 'category'


class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'
    context_object_name = 'portfolios'

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolio'
