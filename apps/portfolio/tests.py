from django.test import TestCase
from .models import Category, Project


class ModelsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            image="test_image.jpg",
            slug="test-category",
        )

        self.category.save()

        self.project = Project.objects.create(
            title="Test Project",
            description="This is a test project.",
            slug="test-project",
            category=self.category,
            image="test_image.jpg",
            url="https://example.com",
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_category_slug(self):
        self.assertEqual(self.category.slug, "test-category")

    def test_project_str(self):
        self.assertEqual(str(self.project), "Test Project")

    def test_project_slug(self):
        self.assertEqual(self.project.slug, "test-project")

    def test_project_category(self):
        self.assertEqual(self.project.category, self.category)