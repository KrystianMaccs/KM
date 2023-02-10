from rest_framework import generics
from rest_framework.response import Response
from apps.portfolio.serializers import CategorySerializer, ProjectSerializer
from rest_framework.exceptions import NotFound
from apps.portfolio.models import Category, Project

class CategoryListOr404(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except Category.DoesNotExist:
            raise NotFound(detail="Category does not exist.")
        

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = ProjectSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            raise NotFound("No projects found.")

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            project = self.get_object()
        except Project.DoesNotExist:
            raise NotFound("Project not found.")
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
