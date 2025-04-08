import json
import uuid

from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from management.service import serv_floor, serv_zone


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

    floor_id = data.get("floor_id")
    floor = serv_floor.get_item(floor_id)
    if not floor:
        return JsonResponse({"error": "Invalid floor_id"}, status=400)

    data["floor"] = floor

    try:
        zone = serv_zone.create_item(data)
        return JsonResponse({"id": str(zone.id)}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def detail(request, zone_id):
    zone = serv_zone.get_item(zone_id)
    if not zone:
        return HttpResponseNotFound("Zone not found")

    return JsonResponse(
        {
            "id": str(zone.id),
            "floor_id": str(zone.floor_id),
            "name": zone.name,
            "metadata": zone.metadata,
            "created_at": zone.created_at.isoformat(),
            "updated_at": zone.updated_at.isoformat(),
        }
    )


def list_by_floor(request, floor_id):
    try:
        floor_id = str(uuid.UUID(str(floor_id)))
        zones = serv_zone.get_items_by_floor(floor_id)

        return JsonResponse(
            {
                "results": [
                    {
                        "id": str(z.id),
                        "floor_id": str(z.floor_id),
                        "name": z.name,
                        "metadata": z.metadata,
                        "created_at": z.created_at.isoformat(),
                        "updated_at": z.updated_at.isoformat(),
                    }
                    for z in zones
                ]
            }
        )
    except ValueError:
        return JsonResponse({"error": "Invalid floor_id format"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def update(request, zone_id):
    if request.method != "PATCH":
        return HttpResponseBadRequest("Method not allowed")

    data = parse_request_data(request)
    if not data:
        return HttpResponseBadRequest("Invalid JSON")

    zone = serv_zone.update_item(zone_id, data)
    if not zone:
        return HttpResponseNotFound("Zone not found")

    return JsonResponse({"id": str(zone.id)})


def delete(request, zone_id):
    success = serv_zone.delete_item(zone_id)
    if not success:
        return HttpResponseNotFound("Zone not found")

    return JsonResponse({"success": True})


def list_items(request):
    result = serv_zone.get_pagination(request.GET)

    return JsonResponse(
        {
            "page": result["page"],
            "total_pages": result["total_pages"],
            "total_items": result["total_items"],
            "has_next": result["has_next"],
            "has_previous": result["has_previous"],
            "results": [
                {
                    "id": str(z.id),
                    "floor_id": str(z.floor_id),
                    "name": z.name,
                    "metadata": z.metadata,
                    "created_at": z.created_at.isoformat(),
                    "updated_at": z.updated_at.isoformat(),
                }
                for z in result["results"]
            ],
        }
    )
