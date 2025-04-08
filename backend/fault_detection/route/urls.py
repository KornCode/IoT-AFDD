from django.urls import path

from .api.handler import hand_alert, hand_config
from .cron.handler import hand_check_disconnect

urlpatterns = [
    # Fault Detection Config
    path("configs/", hand_config.list_items),
    path("configs/create/", hand_config.create),
    path("configs/<uuid:config_id>/", hand_config.detail),
    path("configs/<uuid:config_id>/update/", hand_config.update),
    path("configs/<uuid:config_id>/delete/", hand_config.delete),
    # Fault Detection Cron
    path("alert/<uuid:target_id>/buildings/", hand_alert.list_active_alerts_by_building),
    path("alert/<uuid:target_id>/floors/", hand_alert.list_active_alerts_by_floor),
    path("alert/<uuid:target_id>/zones/", hand_alert.list_active_alerts_by_zone),
    path("alert/<uuid:target_id>/devices/", hand_alert.list_active_alerts_by_device),
    # Acknowledge Fault Alert
    path("alert/<uuid:alert_id>/acknowledge/", hand_alert.acknowledge_alert),
    # Fault Detection Cron
    path("cron/devices/disconnect-alerts/", hand_check_disconnect.publish_disconnect_alert),
]
