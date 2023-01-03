from django.test import TestCase
from apps.portfolio.models import *

class CategoryTestCase(TestCase):
    def setUp(self):
        # Create a new category
        Category.objects.create(name='Test Category')

    def test_generate_unique_slug(self):
        # Create a new category with a name that is already in use
        category = Category.objects.create(name='Test Category')
        # Check that the slug is unique
        self.assertNotEqual(category.slug, 'test-category')

class PortfolioTestCase(TestCase):
    def setUp(self):
        # Create a new category
        self.category = Category.objects.create(name='Test Category')
        # Create a new portfolio
        self.portfolio = Portfolio.objects.create(
            title='Test Portfolio',
            description='This is a test portfolio',
            category=self.category,
            link='http://test.com'
        )

    def test_update(self):
        # Update the portfolio with new data
        self.portfolio.update({
            'title': 'Updated Title',
            'description': 'Updated description',
            'link': 'http://updated.com'
        })
        # Refresh the portfolio from the database
        self.portfolio.refresh_from_db()
        # Check that the fields have been correctly updated
        self.assertEqual(self.portfolio.title, 'Updated Title')
        self.assertEqual(self.portfolio.description, 'Updated description')
        self.assertEqual(self.portfolio.link, 'http://updated.com')


