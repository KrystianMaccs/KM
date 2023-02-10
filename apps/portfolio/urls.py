from django.urls import path
from apps.portfolio.views import CategoryListOr404, ProjectListView, ProjectDetailView


app_name = "portfolios"

urlpatterns = [
    path('categories/', CategoryListOr404.as_view(), name='category-list'),
    path('project_list/', ProjectListView.as_view(), name='project-list'),
    path('str:slug/', ProjectDetailView.as_view(), name='project-detail'),
]
