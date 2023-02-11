from django.db import models
from apps.utils.models import TimeStampedUUIDModel
from django.utils.text import slugify

class Category(TimeStampedUUIDModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True, null=True, blank=True)
    

    def __str__(self):
        return self.name
    
    def save(self, *arg):
        if self.slug is None:
            self.slug = slugify(self.name)
        super(Category, self).save(*arg)
    
    def image_url(self):
        return self.image.url
    
    
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        



class Project(TimeStampedUUIDModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')
    url = models.URLField()
    
    def save(self, *arg):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Project, self).save(*arg)

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        
