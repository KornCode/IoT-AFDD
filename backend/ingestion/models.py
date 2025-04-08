import uuid

from afdd import config
from django.db import models

from .model_enums import DatapointType

PREFIX = f"{config.SUPABASE_DB_PREFIX}ingestion_"


class RawData(models.Model):
    timestamp = models.BigIntegerField()
    datetime = models.DateTimeField()
    device_id = models.TextField()
    datapoint = models.TextField()
    value = models.TextField()

    class Meta:
        db_table = f"{PREFIX}raw_data"
        managed = True

    def delete(self, *args, **kwargs):
        raise NotImplementedError("RawData model is read-only and cannot be deleted.")


class PhysicalQuantity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey("management.Device", on_delete=models.CASCADE, related_name="+")
    datapoint = models.CharField(max_length=50, choices=DatapointType.choices)
    unit = models.CharField(max_length=50, blank=True, null=True)
    formula = models.TextField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{config.SUPABASE_DB_PREFIX}management_physical_quantity"
        managed = False

    def save(self, *args, **kwargs):
        raise NotImplementedError("PhysicalQuantity model is read-only and cannot be saved.")

    def delete(self, *args, **kwargs):
        raise NotImplementedError("PhysicalQuantity model is read-only and cannot be deleted.")
