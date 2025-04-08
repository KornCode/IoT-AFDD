import json
import uuid

from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from management.service import serv_device, serv_physical_quantity


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

    device_id = data.get("device_id")
    device = serv_device.get_item(device_id)
    if not device:
        return JsonResponse({"error": "Invalid device_id"}, status=400)

    data["device"] = device

    try:
        pq = serv_physical_quantity.create_item(data)
        return JsonResponse({"id": str(pq.id)}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def create_many(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Method not allowed")

    data_list = parse_request_data(request)
    if not isinstance(data_list, list):
        return HttpResponseBadRequest("Expected a list of objects")

    for data in data_list:
        device_id = data.get("device_id")
        device = serv_device.get_item(device_id)
        if not device:
            return JsonResponse({"error": f"Invalid device_id: {device_id}"}, status=400)
        data["device"] = device

    try:
        result = serv_physical_quantity.create_items(data_list)
        return JsonResponse({"created": len(result)}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def detail(request, physical_quantity_id):
    pq = serv_physical_quantity.get_item(physical_quantity_id)
    if not pq:
        return HttpResponseNotFound("PhysicalQuantity not found")

    return JsonResponse(
        {
            "id": str(pq.id),
            "device_id": str(pq.device_id),
            "datapoint": pq.datapoint,
            "unit": pq.unit,
            "formula": pq.formula,
            "metadata": pq.metadata,
            "created_at": pq.created_at.isoformat(),
            "updated_at": pq.updated_at.isoformat(),
        }
    )


def list_by_device(request, device_id):
    try:
        device_id = str(uuid.UUID(str(device_id)))
        quantities = serv_physical_quantity.get_items_by_device(device_id)

        return JsonResponse(
            {
                "results": [
                    {
                        "id": str(pq.id),
                        "device_id": str(pq.device_id),
                        "datapoint": pq.datapoint,
                        "unit": pq.unit,
                        "formula": pq.formula,
                        "metadata": pq.metadata,
                        "created_at": pq.created_at.isoformat(),
                        "updated_at": pq.updated_at.isoformat(),
                    }
                    for pq in quantities
                ]
            }
        )

    except ValueError:
        return JsonResponse({"error": "Invalid device_id format"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def update(request, physical_quantity_id):
    if request.method != "PATCH":
        return HttpResponseBadRequest("Method not allowed")

    data = parse_request_data(request)
    if not data:
        return HttpResponseBadRequest("Invalid JSON")

    pq = serv_physical_quantity.update_item(physical_quantity_id, data)
    if not pq:
        return HttpResponseNotFound("PhysicalQuantity not found")

    return JsonResponse({"id": str(pq.id)})


def delete(request, physical_quantity_id):
    success = serv_physical_quantity.delete_item(physical_quantity_id)
    if not success:
        return HttpResponseNotFound("PhysicalQuantity not found")

    return JsonResponse({"success": True})


def list_items(request):
    result = serv_physical_quantity.get_pagination(request.GET)

    return JsonResponse(
        {
            "page": result["page"],
            "total_pages": result["total_pages"],
            "total_items": result["total_items"],
            "has_next": result["has_next"],
            "has_previous": result["has_previous"],
            "results": [
                {
                    "id": str(pq.id),
                    "device_id": str(pq.device_id),
                    "datapoint": pq.datapoint,
                    "unit": pq.unit,
                    "formula": pq.formula,
                    "metadata": pq.metadata,
                    "created_at": pq.created_at.isoformat(),
                    "updated_at": pq.updated_at.isoformat(),
                }
                for pq in result["results"]
            ],
        }
    )
