from rest_framework import generics, views
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
        
class CategoryProjectList(views.APIView):
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)

        projects = Project.objects.filter(category=category)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        try:
            project = self.get_object()
        except Project.DoesNotExist:
            raise NotFound("Project not found.")
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
