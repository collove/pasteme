from django.contrib import admin

from .models import Modal


class ModalAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
        "expires_at",
    ]

    list_display_links = ["id", "name"]

    list_filter = [
        "created_at",
        "expires_at",
    ]

    search_fields = [
        "name",
    ]

    ordering = [
        "created_at",
        "expires_at",
    ]


admin.site.register(Modal, ModalAdmin)
