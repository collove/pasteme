from django.db import models
from shortuuid.django_fields import ShortUUIDField

from .constants import LANGUAGES


class Snippet(models.Model):
    id = ShortUUIDField(
        length=5,
        max_length=40,
        alphabet="abcdefg1234",
        primary_key=True,
    )
    title = models.CharField(
        verbose_name='Title',
        max_length=120,
        default='Untitled',
    )
    body = models.TextField(
        verbose_name='Body'
    )
    language = models.CharField(
        verbose_name='Language',
        max_length=120,
        choices=LANGUAGES,
        default='plaintext',
    )
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now=True,
        editable=False,
    )

    def __str__(self): return f'{self.title} at {self.created_at.date()}'