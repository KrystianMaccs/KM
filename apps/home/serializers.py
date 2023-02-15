from rest_framework import serializers
from apps.home.models import AboutMe, Contact, Resume



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'email', 'subject', 'message')


class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = ('id', 'name', 'description')
        

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'name', 'resume')

