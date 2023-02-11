from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from apps.portfolio.models import Category, Project



@receiver(pre_save, sender=Category)
def category_pre_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)

@receiver(pre_save, sender=Project)
def project_pre_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)



