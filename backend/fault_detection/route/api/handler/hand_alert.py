import json

from django.core.exceptions import ValidationError
from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from fault_detection.service import serv_alert


def acknowledge_alert(request, alert_id):
    if request.method != "PATCH":
        return HttpResponseBadRequest("Method not allowed")

    try:
        data = json.loads(request.body)
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    acknowledged_by = data.get("acknowledged_by")
    include_older = data.get("include_older", True)

    try:
        updated_alerts = serv_alert.acknowledge_item(
            alert_id=alert_id,
            acknowledged_by=acknowledged_by,
            include_older=include_older,
        )
        return JsonResponse(
            {
                "acknowledged_count": len(updated_alerts),
                "acknowledged_alert_ids": [str(alert.id) for alert in updated_alerts],
            }
        )
    except ValidationError as e:
        return HttpResponseBadRequest(str(e))
    except Exception as e:
        return HttpResponseNotFound(str(e))


def list_active_alerts_by_building(request, target_id):
    try:
        alerts = serv_alert.get_items_active_alert_by_building(target_id)
        return JsonResponse({"results": _serialize_alerts(alerts)}, safe=False)
    except ValidationError as e:
        return HttpResponseBadRequest(str(e))


def list_active_alerts_by_floor(request, target_id):
    try:
        alerts = serv_alert.get_items_active_alert_by_floor(target_id)
        return JsonResponse({"results": _serialize_alerts(alerts)}, safe=False)
    except ValidationError as e:
        return HttpResponseBadRequest(str(e))


def list_active_alerts_by_zone(request, target_id):
    try:
        alerts = serv_alert.get_items_active_alert_by_zone(target_id)
        return JsonResponse({"results": _serialize_alerts(alerts)}, safe=False)
    except ValidationError as e:
        return HttpResponseBadRequest(str(e))


def list_active_alerts_by_device(request, target_id):
    try:
        alerts = serv_alert.get_items_active_alert_by_device(target_id)
        return JsonResponse({"results": _serialize_alerts(alerts)}, safe=False)
    except ValidationError as e:
        return HttpResponseBadRequest(str(e))


def _serialize_alerts(alerts):
    return [
        {
            "id": str(alert.id),
            "target_type": alert.target_type,
            "target_id": alert.target_id,
            "datapoint": alert.datapoint,
            "value": alert.value,
            "status": alert.status,
            "alert_mode": alert.alert_mode,
            "alert_time": alert.alert_time.isoformat(),
            "acknowledged_at": alert.acknowledged_at.isoformat() if alert.acknowledged_at else None,
            "acknowledged_by": alert.acknowledged_by,
            "resolved_at": alert.resolved_at.isoformat() if alert.resolved_at else None,
            "resolved_by": alert.resolved_by,
            "metadata": alert.metadata,
        }
        for alert in alerts
    ]
