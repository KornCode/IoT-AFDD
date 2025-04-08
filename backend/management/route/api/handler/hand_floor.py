import json
import uuid

from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from management.service import serv_building, serv_floor


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

    building_id = data.get("building_id")
    building = serv_building.get_item(building_id)

    if not building:
        return JsonResponse({"error": "Invalid building_id"}, status=400)

    data["building"] = building

    try:
        floor = serv_floor.create_item(data)
        return JsonResponse({"id": str(floor.id)}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def detail(request, floor_id):
    floor = serv_floor.get_item(floor_id)
    if not floor:
        return HttpResponseNotFound("Floor not found")

    return JsonResponse(
        {
            "id": str(floor.id),
            "building_id": str(floor.building_id),
            "floor_number": floor.floor_number,
            "name": floor.name,
            "metadata": floor.metadata,
            "created_at": floor.created_at.isoformat(),
            "updated_at": floor.updated_at.isoformat(),
        }
    )


def list_by_building(request, building_id):
    try:
        building_id = str(uuid.UUID(str(building_id)))
        floors = serv_floor.get_items_by_building(building_id)

        return JsonResponse(
            {
                "results": [
                    {
                        "id": str(f.id),
                        "building_id": str(f.building_id),
                        "floor_number": f.floor_number,
                        "name": f.name,
                        "metadata": f.metadata,
                        "created_at": f.created_at.isoformat(),
                        "updated_at": f.updated_at.isoformat(),
                    }
                    for f in floors
                ]
            }
        )
    except ValueError:
        return JsonResponse({"error": "Invalid building_id format"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def update(request, floor_id):
    if request.method != "PATCH":
        return HttpResponseBadRequest("Method not allowed")

    data = parse_request_data(request)
    if not data:
        return HttpResponseBadRequest("Invalid JSON")

    floor = serv_floor.update_item(floor_id, data)
    if not floor:
        return HttpResponseNotFound("Floor not found")

    return JsonResponse({"id": str(floor.id)})


def delete(request, floor_id):
    success = serv_floor.delete_item(floor_id)
    if not success:
        return HttpResponseNotFound("Floor not found")

    return JsonResponse({"success": True})


def list_items(request):
    result = serv_floor.get_pagination(request.GET)

    return JsonResponse(
        {
            "page": result["page"],
            "total_pages": result["total_pages"],
            "total_items": result["total_items"],
            "has_next": result["has_next"],
            "has_previous": result["has_previous"],
            "results": [
                {
                    "id": str(f.id),
                    "building_id": str(f.building_id),
                    "floor_number": f.floor_number,
                    "name": f.name,
                    "metadata": f.metadata,
                    "created_at": f.created_at.isoformat(),
                    "updated_at": f.updated_at.isoformat(),
                }
                for f in result["results"]
            ],
        }
    )
