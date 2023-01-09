from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from apps.portfolio.models import Category, Portfolio
from django.shortcuts import get_object_or_404

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
    context_object_name = 'portfolios'
    template_name = 'portfolio/portfolio_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        """"""
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return self.model.objects.filter(category=category)



class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolio'
