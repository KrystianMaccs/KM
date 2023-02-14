from rest_framework import serializers
from apps.home.models import AboutMe, Navbar, Contact



class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = ('id', 'name', 'slug')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'email', 'subject', 'slug', 'message')


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ('id', 'name', 'resume', 'description')
