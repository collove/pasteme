from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    body = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(unique=True, editable=False)
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)
