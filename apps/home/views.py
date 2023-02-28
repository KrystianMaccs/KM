from rest_framework import generics
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import AllowAny
from apps.home.models import Contact, AboutMe, Resume
from apps.home.serializers import  ContactSerializer, AboutMeSerializer, ResumeSerializer



class ContactList(generics.CreateAPIView):
    serializer_class = ContactSerializer
    email_recipient = settings.CONTACT_EMAIL_RECIPIENT

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # Get the data from the validated serializer
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']

            # Send an email with the data
            subject = 'New contact from {}'.format(name)
            email_body = 'Name: {}\nEmail: {}\nMessage: {}'.format(name, email, message)
            send_mail(subject, email_body, email, [self.email_recipient], fail_silently=False)

            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class AboutMeList(generics.ListCreateAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    
    
@api_view(['GET'])
def download_file(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    serializer = ResumeSerializer(resume)
    filename = resume.file.name
    response = FileResponse(resume.file, as_attachment=True, filename=filename)
    response['Content-Disposition'] = 'attachment; filename="%s"' % filename
    return response