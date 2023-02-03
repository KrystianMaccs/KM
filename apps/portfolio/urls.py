from django.urls import path
from apps.portfolio.views import *


app_name = "portfolio"

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('portfolios/<slug:slug>/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolios/<str:slug>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
]
