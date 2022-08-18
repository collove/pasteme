from django.db import models
from shortuuid.django_fields import ShortUUIDField

from .constants import EXPIRY_OPTIONS, LANGUAGES, THEMES


class Snippet(models.Model):
    id = ShortUUIDField(
        length=5,
        max_length=40,
        alphabet="abcdefg12345",
        primary_key=True,
    )
    title = models.CharField(
        max_length=120,
        default="Untitled",
    )
    body = models.TextField()
    language = models.CharField(
        max_length=120,
        choices=LANGUAGES,
        default="plaintext",
    )
    theme = models.CharField(
        max_length=120,
        default="default",
        choices=THEMES,
    )
    created_at = models.DateTimeField(
        verbose_name="Created at",
        auto_now=True,
        editable=False,
    )
    expires_in = models.SmallIntegerField(
        verbose_name="Expires in",
        choices=EXPIRY_OPTIONS,
        default=7,
    )

    def __str__(self):
        return f"{self.title} at {self.created_at.date()}"
