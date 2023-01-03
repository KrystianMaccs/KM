from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.portfolio.models import Category, Portfolio
#from .forms import CategoryForm, PortfolioForm

class CategoryListView(ListView):
    model = Category
    template_name = 'portfolio/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'portfolio/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    #form_class = CategoryForm
    template_name = 'portfolio/category_create.html'

class CategoryUpdateView(UpdateView):
    model = Category
    #form_class = CategoryForm
    template_name = 'portfolio/category_update.html'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'portfolio/category_delete.html'
    success_url = '/categories/'

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio/portfolio_list.html'
    context_object_name = 'portfolios'

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolio'

class PortfolioCreateView(CreateView):
    model = Portfolio
    #form_class = PortfolioForm
    template_name = 'portfolio/portfolio_create.html'

class PortfolioUpdateView(UpdateView):
    model = Portfolio
    #form_class = PortfolioForm
    template_name = 'portfolio/portfolio_update.html'

class PortfolioDeleteView(DeleteView):
    model = Portfolio
    template_name = 'portfolio/portfolio_delete.html'
    success_url = '/portfolios/'
