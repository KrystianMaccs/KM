from django.urls import path
from . import views


app_name = "portfolio"

urlpatterns = [
    path('portfolios/', views.PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolios/<int:pk>/', views.PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('portfolios/create/', views.PortfolioCreateView.as_view(), name='portfolio_create'),
    path('portfolios/<slug:slug>/update/', views.PortfolioUpdateView.as_view(), name='portfolio_update'),
    path('portfolios/<slug:slug>/delete/', views.PortfolioDeleteView.as_view(), name='portfolio_delete'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<slug:slug>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<slug:slug>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
]
