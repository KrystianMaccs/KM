from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('list/', views.CategoryListView.as_view(), name='list'),
    path('<slug:slug>/', views.CategoryDetailView.as_view(), name='detail'),
    path('create/', views.CategoryCreateView.as_view(), name='create'),
    path('<slug:slug>/update/', views.CategoryUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.CategoryDeleteView.as_view(), name='delete'),
]
