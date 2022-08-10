import json
from os import path

import pypistats
import requests
from django.core.management.base import BaseCommand

from pypi.models import Statistic
from pypi.constants import GITHUB_API_ROOT


class Command(BaseCommand):
    help = "Collects the package stats from PyPIstats and Github."

    def handle(self, *args, **options):
        pasteme_totlal_stars = int(
            requests.get(path.join(GITHUB_API_ROOT, "repos/collove/pasteme")).json()[
                "stargazers_count"
            ]
        )
        pastemecli_totlal_stars = int(
            requests.get(path.join(GITHUB_API_ROOT, "repos/collove/pasteme-cli")).json()[
                "stargazers_count"
            ]
        )
        daily_payload = json.loads(pypistats.recent("pasteme-cli", format="json"))[
            "data"
        ]
        overall_downloads = json.loads(pypistats.overall("pasteme-cli", format="json"))[
            "data"
        ][0]["downloads"]

        obj = Statistic(
            last_day_downloads=daily_payload["last_day"],
            last_week_downloads=daily_payload["last_week"],
            last_month_downloads=daily_payload["last_month"],
            total_downloads=overall_downloads,
            total_service_stars=pasteme_totlal_stars,
            total_package_stars=pastemecli_totlal_stars,
        )
        
        try:
            obj.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f"New Statistics objects collected w/ NO.{obj}!"
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    f"For some reason ({e}), I couldn't generate a new Statistics object!"
                )
            )
