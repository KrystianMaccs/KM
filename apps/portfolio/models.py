from django.db import models
from apps.utils.models import TimeStampedUUIDModel


class Category(TimeStampedUUIDModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    def image_url(self):
        return self.image.url
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


"""class Portfolio(TimeStampedUUIDModel):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=200, default='', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    image = CloudinaryField("featured image", blank=True)
    link = models.URLField(max_length=255, default='')"""