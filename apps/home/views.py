from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from apps.home.models import Navbar, Contact, AboutMe
from apps.home.serializers import NavbarSerializer, ContactSerializer, AboutMeSerializer

class NavbarList(generics.ListCreateAPIView):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer
    lookup_field = 'slug'

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AboutMeList(generics.ListCreateAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

"""class AboutMeDetail(APIView):
    def get_object(self):
        try:
            return AboutMe.objects.all()
        except AboutMe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        about_me = self.get_object(pk)
        serializer = AboutMeSerializer(about_me)
        return Response(serializer.data)

    def get_resume(self, request, pk):
        about_me = self.get_object(pk)
        file = about_me.resume.path
        return FileResponse(open(file, 'rb'))

"""