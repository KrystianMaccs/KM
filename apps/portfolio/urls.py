from django.urls import path
from apps.portfolio.views import CategoryListOr404


app_name = "portfolios"

urlpatterns = [
    path('categories/', CategoryListOr404.as_view(), name='category-list'),
]
