from django.db import models
import uuid
from django.utils.text import slugify

from apps.utils.models import TimeStampedUUIDModel

class Category(TimeStampedUUIDModel):
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=200, default='', blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super(Category, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.name)
        while Category.objects.filter(slug=slug).exists():
            # Generate a random hexadecimal string of length 12
            random_string = uuid.uuid4().hex[:12]
            slug = slugify(self.name + '-' + random_string)
        return slug

class Portfolio(TimeStampedUUIDModel):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    #image = CloudinaryField("featured image", blank=True)
    link = models.URLField(max_length=255, default='')

    def __str__(self):
        return self.title
    
    def update(self, data):
        self.title = data.get('title', self.title)
        self.description = data.get('description', self.description)
        self.category = data.get('category', self.category)
        #self.image = data.get('image', self.image)
        self.link = data.get('link', self.link)
        self.save()

    def delete(self):
        self.delete()