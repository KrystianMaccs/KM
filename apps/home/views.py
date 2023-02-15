from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from apps.home.models import Contact, AboutMe
from apps.home.serializers import  ContactSerializer, AboutMeSerializer

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AboutMeList(generics.ListCreateAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
