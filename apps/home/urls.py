from django.urls import path
from apps.home.views import NavbarList, ContactList, AboutMeList

urlpatterns = [
    path('navbar/', NavbarList.as_view(), name='navbar'),
    path('contact/', ContactList.as_view(), name='contact'),
    path('aboutme/', AboutMeList.as_view(), name='about-me'),
    #path('aboutme/<int:pk>/', AboutMeDetail.as_view(), 'about-me-detail'),
    #path('aboutme/<int:pk>/resume/', AboutMeDetail.get_resume),
]