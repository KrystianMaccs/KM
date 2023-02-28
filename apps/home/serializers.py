from rest_framework import serializers
from apps.home.models import AboutMe, Contact, Resume

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.

    Includes fields 'id', 'email', 'subject', and 'message'.
    """
    class Meta:
        model = Contact
        fields = ('id', 'email', 'name', 'message')

class AboutMeSerializer(serializers.ModelSerializer):
    """
    Serializer for the AboutMe model.

    Includes fields 'id', 'name', and 'description'.
    """
    class Meta:
        model = AboutMe
        fields = ('id', 'name', 'description')

class ResumeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Resume model.

    Includes fields 'id', 'file', and 'name', where 'file' is a URL representing
    the file data rather than the data itself.
    """
    file = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = Resume
        fields = ('id', 'file', 'name')
