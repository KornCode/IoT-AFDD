import uuid

from afdd import config
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from fault_detection.model_enums import (
    AggregationType,
    AlertMode,
    DatapointType,
    DeviceType,
    TargetType,
)

PREFIX = f"{config.SUPABASE_DB_PREFIX}fault_detection_"


class FaultDetectionConfig(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    target_type = models.CharField(max_length=20, choices=TargetType.choices)
    target_id = models.CharField(max_length=100)
    datapoint = models.CharField(max_length=50, choices=DatapointType.choices)
    aggregation = models.CharField(
        max_length=10,
        choices=AggregationType.choices,
        default=AggregationType.NONE,
        help_text="Use 'none' for device-level rules",
    )
    min_value = models.FloatField(null=True, blank=True)
    max_value = models.FloatField(null=True, blank=True)
    logic_expression = models.TextField(null=True, blank=True, help_text="e.g. x < 18 or x > 28")
    priority = models.IntegerField(default=10, help_text="Lower = higher priority")
    enabled = models.BooleanField(default=True)
    alert_repeat_interval_minutes = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1)],
        help_text="Repeat alerts every X minutes while fault persists (must be ≥ 1)",
    )
    alert_data_silence_threshold_minutes = models.IntegerField(
        null=True, blank=True, help_text="Trigger alert if no data is received in this many minutes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{PREFIX}config"
        managed = True
        indexes = [
            models.Index(fields=["target_type", "target_id"]),
            models.Index(fields=["datapoint"]),
        ]


class FaultSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    config = models.ForeignKey(FaultDetectionConfig, on_delete=models.CASCADE, related_name="sessions")
    target_type = models.CharField(max_length=20, choices=TargetType.choices)
    target_id = models.CharField(max_length=100)
    datapoint = models.CharField(max_length=50, choices=DatapointType.choices)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = f"{PREFIX}session"
        managed = True
        indexes = [
            models.Index(fields=["target_type", "target_id"]),
            models.Index(fields=["datapoint"]),
            models.Index(fields=["is_active"]),
        ]


class FaultAlert(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey("FaultSession", on_delete=models.SET_NULL, null=True, blank=True, related_name="alerts")
    config = models.ForeignKey(
        "FaultDetectionConfig", on_delete=models.SET_NULL, null=True, blank=True, related_name="alerts"
    )
    target_type = models.CharField(max_length=20, choices=TargetType.choices)
    target_id = models.CharField(max_length=100)
    resolved_building_id = models.UUIDField(null=True, blank=True)
    resolved_floor_id = models.UUIDField(null=True, blank=True)
    resolved_zone_id = models.UUIDField(null=True, blank=True)
    resolved_device_id = models.UUIDField(null=True, blank=True)
    datapoint = models.CharField(max_length=50, choices=DatapointType.choices)
    value = models.FloatField(null=True, blank=True)
    alert_mode = models.CharField(
        max_length=20,
        choices=AlertMode.choices,
        default=AlertMode.THRESHOLD,
        help_text="Type of fault alert: threshold or disconnect",
    )
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("acknowledged", "Acknowledged"), ("resolved", "Resolved")],
        default="active",
    )
    alert_time = models.DateTimeField(default=timezone.now)
    acknowledged_at = models.DateTimeField(null=True, blank=True)
    acknowledged_by = models.CharField(max_length=100, null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolved_by = models.CharField(max_length=100, null=True, blank=True)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{PREFIX}alert"
        managed = True
        indexes = [
            models.Index(fields=["target_type", "target_id"]),
            models.Index(fields=["datapoint"]),
            models.Index(fields=["status"]),
            models.Index(fields=["alert_time"]),
            models.Index(fields=["resolved_building_id"]),
            models.Index(fields=["resolved_floor_id"]),
            models.Index(fields=["resolved_zone_id"]),
            models.Index(fields=["resolved_device_id"]),
        ]


class Floor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    building = models.ForeignKey("management.Building", on_delete=models.CASCADE, related_name="+")
    floor_number = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{config.SUPABASE_DB_PREFIX}management_floor"
        managed = False


class Zone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    floor = models.ForeignKey("management.Floor", on_delete=models.CASCADE, related_name="+")
    name = models.CharField(max_length=255)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{config.SUPABASE_DB_PREFIX}management_zone"
        managed = False


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    building = models.ForeignKey("management.Building", on_delete=models.CASCADE, related_name="+")
    floor = models.ForeignKey("management.Floor", on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    zone = models.ForeignKey("management.Zone", on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    name = models.CharField(max_length=255)
    device_type = models.CharField(max_length=50, choices=DeviceType.choices)
    serial_number = models.CharField(max_length=100, unique=True)
    install_date = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = f"{config.SUPABASE_DB_PREFIX}management_device"
        managed = False


class RawData(models.Model):
    timestamp = models.BigIntegerField()
    datetime = models.DateTimeField()
    device_id = models.TextField()
    datapoint = models.TextField()
    value = models.TextField()

    class Meta:
        db_table = f"{config.SUPABASE_DB_PREFIX}ingestion_raw_data"
        managed = False

    def save(self, *args, **kwargs):
        raise NotImplementedError("RawData model is read-only and cannot be saved.")

    def delete(self, *args, **kwargs):
        raise NotImplementedError("RawData model is read-only and cannot be deleted.")
