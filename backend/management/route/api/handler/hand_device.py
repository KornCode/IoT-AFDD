import json
import uuid

from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from management.service import serv_building, serv_device, serv_zone


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

    zone_id = data.get("zone_id")
    building_id = data.get("building_id")

    if zone_id:
        zone = serv_zone.get_item(zone_id)
        if not zone:
            return JsonResponse({"error": "Invalid zone_id"}, status=400)
        data["zone"] = zone

    if building_id:
        building = serv_building.get_item(building_id)
        if not building:
            return JsonResponse({"error": "Invalid building_id"}, status=400)
        data["building"] = building

    try:
        device = serv_device.create_item(data)
        return JsonResponse({"id": str(device.id)}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def detail(request, device_id):
    device = serv_device.get_item(device_id)
    if not device:
        return HttpResponseNotFound("Device not found")

    return JsonResponse(
        {
            "id": str(device.id),
            "zone_id": str(device.zone_id) if device.zone_id else None,
            "building_id": str(device.building_id) if device.building_id else None,
            "name": device.name,
            "device_type": device.device_type,
            "serial_number": device.serial_number,
            "install_date": device.install_date.isoformat() if device.install_date else None,
            "metadata": device.metadata,
            "created_at": device.created_at.isoformat(),
            "updated_at": device.updated_at.isoformat(),
        }
    )


def list_by_building(request, building_id):
    try:
        building_id = str(uuid.UUID(str(building_id)))
        devices = serv_device.get_items_by_building(building_id)

        return JsonResponse(
            {
                "results": [
                    {
                        "id": str(d.id),
                        "zone_id": str(d.zone_id) if d.zone_id else None,
                        "floor_id": str(d.floor_id) if d.floor_id else None,
                        "building_id": str(d.building_id),
                        "name": d.name,
                        "device_type": d.device_type,
                        "serial_number": d.serial_number,
                        "install_date": d.install_date.isoformat() if d.install_date else None,
                        "metadata": d.metadata,
                        "created_at": d.created_at.isoformat(),
                        "updated_at": d.updated_at.isoformat(),
                    }
                    for d in devices
                ]
            }
        )
    except ValueError:
        return JsonResponse({"error": "Invalid building_id format"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def list_by_floor(request, floor_id):
    try:
        floor_id = str(uuid.UUID(str(floor_id)))
        devices = serv_device.get_items_by_floor(floor_id)

        return JsonResponse(
            {
                "results": [
                    {
                        "id": str(d.id),
                        "zone_id": str(d.zone_id) if d.zone_id else None,
                        "floor_id": str(d.floor_id),
                        "building_id": str(d.building_id) if d.building_id else None,
                        "name": d.name,
                        "device_type": d.device_type,
                        "serial_number": d.serial_number,
                        "install_date": d.install_date.isoformat() if d.install_date else None,
                        "metadata": d.metadata,
                        "created_at": d.created_at.isoformat(),
                        "updated_at": d.updated_at.isoformat(),
                    }
                    for d in devices
                ]
            }
        )
    except ValueError:
        return JsonResponse({"error": "Invalid floor_id format"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def list_by_zone(request, zone_id):
    try:
        zone_id = str(uuid.UUID(str(zone_id)))
        devices = serv_device.get_items_by_zone(zone_id)

        return JsonResponse(
            {
                "results": [
                    {
                        "id": str(d.id),
                        "zone_id": str(d.zone_id),
                        "floor_id": str(d.floor_id) if d.floor_id else None,
                        "building_id": str(d.building_id) if d.building_id else None,
                        "name": d.name,
                        "device_type": d.device_type,
                        "serial_number": d.serial_number,
                        "install_date": d.install_date.isoformat() if d.install_date else None,
                        "metadata": d.metadata,
                        "created_at": d.created_at.isoformat(),
                        "updated_at": d.updated_at.isoformat(),
                    }
                    for d in devices
                ]
            }
        )
    except ValueError:
        return JsonResponse({"error": "Invalid zone_id format"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def update(request, device_id):
    if request.method != "PATCH":
        return HttpResponseBadRequest("Method not allowed")

    data = parse_request_data(request)
    if not data:
        return HttpResponseBadRequest("Invalid JSON")

    device = serv_device.update_item(device_id, data)
    if not device:
        return HttpResponseNotFound("Device not found")

    return JsonResponse({"id": str(device.id)})


def delete(request, device_id):
    success = serv_device.delete_item(device_id)
    if not success:
        return HttpResponseNotFound("Device not found")

    return JsonResponse({"success": True})


def list_items(request):
    result = serv_device.get_pagination(request.GET)

    return JsonResponse(
        {
            "page": result["page"],
            "total_pages": result["total_pages"],
            "total_items": result["total_items"],
            "has_next": result["has_next"],
            "has_previous": result["has_previous"],
            "results": [
                {
                    "id": str(d.id),
                    "zone_id": str(d.zone_id) if d.zone_id else None,
                    "building_id": str(d.building_id) if d.building_id else None,
                    "name": d.name,
                    "device_type": d.device_type,
                    "serial_number": d.serial_number,
                    "install_date": d.install_date.isoformat() if d.install_date else None,
                    "metadata": d.metadata,
                    "created_at": d.created_at.isoformat(),
                    "updated_at": d.updated_at.isoformat(),
                }
                for d in result["results"]
            ],
        }
    )
