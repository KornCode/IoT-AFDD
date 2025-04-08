import json

from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from management.service import serv_building


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
        building = serv_building.create_item(data)
        return JsonResponse({"id": str(building.id)}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def detail(request, building_id):
    building = serv_building.get_item(building_id)
    if not building:
        return HttpResponseNotFound("Building not found")

    return JsonResponse(
        {
            "id": str(building.id),
            "name": building.name,
            "type": building.type,
            "address": building.address,
            "metadata": building.metadata,
            "created_at": building.created_at.isoformat(),
            "updated_at": building.updated_at.isoformat(),
        }
    )


def update(request, building_id):
    if request.method != "PATCH":
        return HttpResponseBadRequest("Method not allowed")

    data = parse_request_data(request)
    if not data:
        return HttpResponseBadRequest("Invalid JSON")

    building = serv_building.update_item(building_id, data)
    if not building:
        return HttpResponseNotFound("Building not found")

    return JsonResponse({"id": str(building.id)})


def delete(request, building_id):
    success = serv_building.delete_item(building_id)
    if not success:
        return HttpResponseNotFound("Building not found")

    return JsonResponse({"success": True})


def list_items(request):
    result = serv_building.get_pagination(request.GET)

    return JsonResponse(
        {
            "page": result["page"],
            "total_pages": result["total_pages"],
            "total_items": result["total_items"],
            "has_next": result["has_next"],
            "has_previous": result["has_previous"],
            "results": [
                {
                    "id": str(b.id),
                    "name": b.name,
                    "type": b.type,
                    "address": b.address,
                    "metadata": b.metadata,
                    "created_at": b.created_at.isoformat(),
                    "updated_at": b.updated_at.isoformat(),
                }
                for b in result["results"]
            ],
        }
    )
