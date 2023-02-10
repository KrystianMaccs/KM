from rest_framework import generics
from apps.portfolio.serializers import CategorySerializer
from rest_framework.exceptions import NotFound
from apps.portfolio.models import Category

class CategoryListOr404(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except Category.DoesNotExist:
            raise NotFound(detail="Category does not exist.")

