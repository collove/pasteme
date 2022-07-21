from django.db import models


class Statistic(models.Model):
    last_day_downloads = models.PositiveIntegerField()
    last_week_downloads = models.PositiveIntegerField()
    last_month_downloads = models.PositiveIntegerField()
    total_downloads = models.PositiveIntegerField()
    total_service_stars = models.PositiveIntegerField()
    total_package_stars = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self): return f'{self.id} at {self.date}'