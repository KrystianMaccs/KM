from django.urls import path
from apps.portfolio.views import *


app_name = "portfolio"

urlpatterns = [
    path('portfolio/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('portfolios/create/', PortfolioCreateView.as_view(), name='portfolio_create'),
    path('portfolios/<int:pk>/update/', PortfolioUpdateView.as_view(), name='portfolio_update'),
    path('portfolios/<int:pk>/delete/', PortfolioDeleteView.as_view(), name='portfolio_delete'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
