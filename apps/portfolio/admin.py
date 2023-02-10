from django.contrib import admin

from apps.portfolio.models import Category, Project

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'image', 'url']
