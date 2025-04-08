import json

from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from fault_detection.service import serv_config


def parse_request_data(request):
    try:
        return json.loads(request.body)
    except Exception:
        return None


def create(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Method not allowed")

    data = parse_request_data(request)
    if not data:
        return HttpResponseBadRequest("Invalid JSON")

    try:
        config = serv_config.create_item(data)
        return JsonResponse({"id": str(config.id)}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def detail(request, config_id):
    config = serv_config.get_item(config_id)
    if not config:
        return HttpResponseNotFound("Config not found")

    return JsonResponse(
        {
            "id": str(config.id),
            "target_type": config.target_type,
            "target_id": config.target_id,
            "datapoint": config.datapoint,
            "aggregation": config.aggregation,
            "min_value": config.min_value,
            "max_value": config.max_value,
            "logic_expression": config.logic_expression,
            "priority": config.priority,
            "enabled": config.enabled,
            "alert_repeat_interval_minutes": config.alert_repeat_interval_minutes,
            "alert_data_silence_threshold_minutes": config.alert_data_silence_threshold_minutes,
            "created_at": config.created_at.isoformat(),
            "updated_at": config.updated_at.isoformat(),
        }
    )


def update(request, config_id):
    if request.method != "PATCH":
        return HttpResponseBadRequest("Method not allowed")

    data = parse_request_data(request)
    if not data:
        return HttpResponseBadRequest("Invalid JSON")

    config = serv_config.update_item(config_id, data)
    if not config:
        return HttpResponseNotFound("Config not found")

    return JsonResponse({"id": str(config.id)})


def delete(request, config_id):
    success = serv_config.delete_item(config_id)
    if not success:
        return HttpResponseNotFound("Config not found")

    return JsonResponse({"success": True})


def list_items(request):
    result = serv_config.get_pagination(request.GET)

    return JsonResponse(
        {
            "page": result["page"],
            "total_pages": result["total_pages"],
            "total_items": result["total_items"],
            "has_next": result["has_next"],
            "has_previous": result["has_previous"],
            "results": [
                {
                    "id": str(c.id),
                    "target_type": c.target_type,
                    "target_id": c.target_id,
                    "datapoint": c.datapoint,
                    "aggregation": c.aggregation,
                    "min_value": c.min_value,
                    "max_value": c.max_value,
                    "logic_expression": c.logic_expression,
                    "priority": c.priority,
                    "enabled": c.enabled,
                    "alert_repeat_interval_minutes": c.alert_repeat_interval_minutes,
                    "alert_data_silence_threshold_minutes": c.alert_data_silence_threshold_minutes,
                    "created_at": c.created_at.isoformat(),
                    "updated_at": c.updated_at.isoformat(),
                }
                for c in result["results"]
            ],
        }
    )
