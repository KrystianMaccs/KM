from django.urls import path
from apps.portfolio.views import *


app_name = "portfolio"

urlpatterns = [
    path('portfolios/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolios/<slug:slug>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('portfolios/create/', PortfolioCreateView.as_view(), name='portfolio_create'),
    path('portfolios/<slug:slug>/update/', PortfolioUpdateView.as_view(), name='portfolio_update'),
    path('portfolios/<slug:slug>/delete/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<slug:slug>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
