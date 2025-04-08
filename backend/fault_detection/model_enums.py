from django.db import models


class AlertMode(models.TextChoices):
    THRESHOLD = "threshold", "Threshold"
    DISCONNECT = "disconnect", "Disconnect"


class TargetType(models.TextChoices):
    BUILDING = "building", "Building"
    FLOOR = "floor", "Floor"
    ZONE = "zone", "Zone"
    DEVICE = "device", "Device"


class AggregationType(models.TextChoices):
    AVG = "avg", "Average"
    SUM = "sum", "Sum"
    MIN = "min", "Minimum"
    MAX = "max", "Maximum"
    NONE = "none", "None"


class DatapointType(models.TextChoices):
    TEMPERATURE = "temperature", "Temperature"
    HUMIDITY = "humidity", "Humidity"
    CO2 = "co2", "CO₂"
    PRESENCE_STATE = "presence_state", "Presence State"
    SENSITIVITY = "sensitivity", "Sensitivity"
    ONLINE_STATUS = "online_status", "Online Status"
    POWER = "power", "Power Consumption"


class DeviceType(models.TextChoices):
    IAQ = "iaq", "Indoor Air Quality"
    OAQ = "oaq", "Outdoor Air Quality"
    PRESENCE = "presence", "Presence"
    ENERGY = "energy", "Energy"


class DatapointType(models.TextChoices):
    TEMPERATURE = "temperature", "Temperature"
    HUMIDITY = "humidity", "Humidity"
    CO2 = "co2", "CO₂"
    PRESENCE_STATE = "presence_state", "Presence State"
    SENSITIVITY = "sensitivity", "Sensitivity"
    ONLINE_STATUS = "online_status", "Online Status"
    POWER = "power", "Power Consumption"
