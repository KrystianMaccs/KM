from django.views.generic import ListView, DetailView

from apps.portfolio.models import Category, Portfolio
from django.shortcuts import get_object_or_404

class CategoryListView(ListView):
    model = Category
    template_name = 'portfolio/category_list.html'
    context_object_name = 'categories'

class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = 'portfolios'
    template_name = 'portfolio/portfolio_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context




class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolios'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = get_object_or_404(Portfolio, slug=self.kwargs['slug'])
        return context
