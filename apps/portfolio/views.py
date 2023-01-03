from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.portfolio.models import Category, Portfolio
#from .forms import CategoryForm, PortfolioForm

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    #form_class = CategoryForm
    template_name = 'category_create.html'

class CategoryUpdateView(UpdateView):
    model = Category
    #form_class = CategoryForm
    template_name = 'category_update.html'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = '/categories/'

class PortfolioListView(ListView):
    model = Portfolio
    template_name = 'portfolio_list.html'
    context_object_name = 'portfolios'

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_detail.html'
    context_object_name = 'portfolio'

class PortfolioCreateView(CreateView):
    model = Portfolio
    #form_class = PortfolioForm
    template_name = 'portfolio_create.html'

class PortfolioUpdateView(UpdateView):
    model = Portfolio
    #form_class = PortfolioForm
    template_name = 'portfolio_update.html'

class PortfolioDeleteView(DeleteView):
    model = Portfolio
    template_name = 'portfolio_delete.html'
    success_url = '/portfolios/'
