from django.core.exceptions import ValidationError
from django.db import models


class Modal(models.Model):
    def validate_file_extension(file):
        if not file.name.endswith(".png"):
            raise ValidationError("Only .png files are allowed.")

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=400)

    footer_title = models.CharField(max_length=255, blank=True, null=True)
    footer_description = models.TextField(max_length=400, blank=True, null=True)

    icon = models.FileField(
        upload_to="modal/icon/", validators=[validate_file_extension]
    )

    external_link = models.URLField(blank=True, null=True)
    expires_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
