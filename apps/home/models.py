from django.db import models
from apps.utils.models import TimeStampedUUIDModel
from django.utils.text import slugify

class Navbar(TimeStampedUUIDModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    class Meta:
        verbose_name = "Navbar"
        verbose_name_plural = "Navbars"

    def __str__(self):
        return self.name
    
    def save(self, *arg, **kwargs):
        self.slug = slugify(self.name)
        super(Navbar, self).save(arg, kwargs)
    
class Contact(TimeStampedUUIDModel):
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, null=True, blank=True)
    message = models.TextField()
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.email

class AboutMe(TimeStampedUUIDModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.name
    
    def save(self, *arg, **kwargs):
        self.slug = slugify(self.name)
        super().save(arg, kwargs)
        
class Resume(TimeStampedUUIDModel):
    name = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name
