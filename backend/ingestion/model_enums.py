from django.db import models


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
