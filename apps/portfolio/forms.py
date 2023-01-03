from django.forms import ModelForm
from apps.portfolio.models import Portfolio, Category

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'category', 'link']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']