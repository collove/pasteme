from os import path

import requests
from django.core.management.base import BaseCommand

DOWNLOAD_URL = "https://contrib.rocks/preview?repo=collove%2Fpasteme"


class Command(BaseCommand):
    help = "Updates the contributors image on the homepage"

    def handle(self, *args, **options):
        CUR_DIR = path.dirname(path.realpath(__file__))
        STAT_FILES_DIR = path.join(CUR_DIR, "../../../snippet/static/img/")
        try:
            response = requests.get(DOWNLOAD_URL)
            if response.status_code == 200:
                with open(path.join(STAT_FILES_DIR, "contributors.svg"), "wb") as f:
                    f.write(response.content)
                    self.stdout.write(
                        self.style.SUCCESS("Successfully updated contributors image")
                    )
            else:
                raise Exception("Could not download contributors image")
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error updating contributors image: {e}")
            )
