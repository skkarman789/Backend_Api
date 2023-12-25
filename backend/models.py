from django.db import models
from datetime import datetime, timezone


class Data(models.Model):
    timestamp = models.DateTimeField()
    is_overspeeding = models.BooleanField(default=False)
    vehicle_no = models.CharField(max_length=255)
    location_type = models.TextField(max_length=255)

    def __str__(self):
        return f"Data - {self.vehicle_no} - {self.timestamp}"


class AlertThreshold(models.Model):
    location_type = models.CharField(max_length=255, unique=True)
    threshold = models.IntegerField()

    def __str__(self):
        return f"{self.location_type} - {self.threshold}"

    def save(self, *args, **kwargs):
        if self.threshold is None:
            default_thresholds = {
                'highway': 4,
                'city_center': 3,
                'commercial': 2,
                'residential': 1,
            }
            self.threshold = default_thresholds.get(self.location_type, 1)

        super().save(*args, **kwargs)


class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    location_type = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now(timezone.utc)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Alert {self.alert_id}- {self.location_type}"
