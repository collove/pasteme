import json

import pypistats
import requests
from django.core.management.base import BaseCommand

from pypi.models import Statistic


class Command(BaseCommand):
    help = 'Collects stats of pasteme-cli package using pypistats SDK'

    def handle(self, *args, **options):
        pasteme_totlal_stars = int(requests.get('https://api.github.com/repos/collove/pasteme').json()['stargazers_count'])
        pastemecli_totlal_stars = int(requests.get('https://api.github.com/repos/collove/pasteme-cli').json()['stargazers_count'])
        daily_payload = json.loads(pypistats.recent("pasteme-cli", format="json"))['data']
        overall_downloads = json.loads(pypistats.overall('pasteme-cli', format='json'))['data'][0]['downloads']
        
        obj = Statistic(
            last_day_downloads=daily_payload['last_day'],
            last_week_downloads=daily_payload['last_week'],
            last_month_downloads=daily_payload['last_month'],
            total_downloads=overall_downloads,
            total_service_stars=pasteme_totlal_stars,
            total_package_stars=pastemecli_totlal_stars,
        )
        
        obj.save()
        
        self.stdout.write(f'Statistics {obj} object created!')