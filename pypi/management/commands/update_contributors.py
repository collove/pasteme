from os import path

import urllib.request as request
from django.core.management.base import BaseCommand

from pypi.constants import DOWNLOAD_URL


class Command(BaseCommand):
    help = "Updates the contributors image on the homepage"

    def handle(self, *args, **options):
        CUR_DIR = path.dirname(path.realpath(__file__))
        STAT_FILES_DIR = path.join(CUR_DIR, "../../../snippet/static/img/")
        try:
            request.urlretrieve(
                DOWNLOAD_URL, path.join(STAT_FILES_DIR, "contributors.svg")
            )
            self.stdout.write(
                self.style.SUCCESS("Successfully updated contributors image")
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error updating contributors image: {e}")
            )
