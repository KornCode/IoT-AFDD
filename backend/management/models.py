import uuid

from afdd import config
from django.core.exceptions import ValidationError
from django.db import models

from .model_enums import BuildingType, DatapointType, DeviceType

PREFIX = f"{config.SUPABASE_DB_PREFIX}management_"


class Building(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=BuildingType.choices)
    address = models.TextField()
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{PREFIX}building"
        managed = True


class Floor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    building = models.ForeignKey("Building", on_delete=models.CASCADE, related_name="floors")
    floor_number = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{PREFIX}floor"
        managed = True
        unique_together = ("building", "floor_number")


class Zone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    floor = models.ForeignKey("Floor", on_delete=models.CASCADE, related_name="zones")
    name = models.CharField(max_length=255)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{PREFIX}zone"
        managed = True
        unique_together = ("floor", "name")


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    building = models.ForeignKey("Building", on_delete=models.CASCADE, related_name="devices")
    floor = models.ForeignKey("Floor", on_delete=models.SET_NULL, null=True, blank=True, related_name="devices")
    zone = models.ForeignKey("Zone", on_delete=models.SET_NULL, null=True, blank=True, related_name="devices")
    name = models.CharField(max_length=255)
    device_type = models.CharField(max_length=50, choices=DeviceType.choices)
    serial_number = models.CharField(max_length=100, unique=True)
    install_date = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{PREFIX}device"
        managed = True

    def clean(self):
        # Ensure either zone, floor, or none — but not inconsistent
        if self.zone and self.floor and self.zone.floor_id != self.floor.id:
            raise ValidationError("Zone must belong to the selected floor.")

        if self.floor and self.floor.building_id != self.building_id:
            raise ValidationError("Floor must belong to the selected building.")

        if self.zone and self.zone.floor.building_id != self.building_id:
            raise ValidationError("Zone must belong to the selected building.")


class PhysicalQuantity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey("Device", on_delete=models.CASCADE, related_name="physical_quantities")
    datapoint = models.CharField(max_length=50, choices=DatapointType.choices)
    unit = models.CharField(max_length=50, blank=True, null=True)
    formula = models.TextField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{PREFIX}physical_quantity"
        managed = True
        constraints = [models.UniqueConstraint(fields=["device", "datapoint"], name="unique_device_datapoint_formula")]
