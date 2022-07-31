from shortuuid.django_fields import ShortUUIDField
from django.db import models


from .constants import LANGUAGES, THEMES


class Snippet(models.Model):
    class ExpiryOptions(models.TextChoices):
        ONE_DAY = "1d", "One Day"
        ONE_WEEK = "1w", "One Week"
        ONE_MONTH = "1m", "One Month"

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
    expires_at = models.CharField(
        max_length=2,
        choices=ExpiryOptions.choices,
        default=ExpiryOptions.ONE_DAY,
    )

    def __str__(self):
        return f"{self.title} at {self.created_at.date()}"
