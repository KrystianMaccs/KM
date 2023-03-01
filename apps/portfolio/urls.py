from django.urls import path
from apps.portfolio.views import CategoryListOr404, ProjectDetailView, CategoryProjectList


app_name = "portfolios"

urlpatterns = [
    path('categories/', CategoryListOr404.as_view(), name='category-list'),
    path('category-projects/<str:slug>/', CategoryProjectList.as_view(), name='project-list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail')

    #path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
]
