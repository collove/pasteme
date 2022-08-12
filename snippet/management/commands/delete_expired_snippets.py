from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import F

from snippet.models import Snippet


class Command(BaseCommand):
    help = "Removes expired snippets."

    def handle(self, *args, **options):
        expired_snippets = Snippet.objects.filter(
            expires_in__lt=timezone.now().date() - F("created_at__date"),
        )
        
        expired_snippets_count = expired_snippets.count()
        expired_snippets.delete()
        
        if expired_snippets_count:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{expired_snippets_count} snippet(s) removed!"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"No snippets expires today!"
                )
            )