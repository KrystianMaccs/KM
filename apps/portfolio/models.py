import uuid
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
    detail = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    image = CloudinaryField("featured image", blank=True)
    link = models.CharField(max_length=255, default='')

    def _str_(self):
        return self.title