# Project: AFDD
Automatic Fault Detection and Diagnostic
# 📁 Collection: Management 
Manage CRUD for buildings, floors, zones, devices, and physical quantities. 

## 📁 Collection: Building 
undefined 


## End-point: Create
Generated from cURL: curl -X POST http://localhost:5005/management/buildings/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Smart Hotel",
    "type": "hotel",
    "address": "123 IoT Blvd",
    "metadata": {
      "floors": 10,
      "smart_enabled": true
    }
  }'
### Method: POST
>```
>{{base_url}}/management/buildings/create/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "name": "3 Seasons Hotel",
    "type": "hotel",
    "address": "123 IoT Blvd",
    "metadata": {}
  }
```

### Response: 201
```json
{
    "id": "3f52bef7-001f-4844-a5fb-e209d769140a"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update
Generated from cURL: curl -X PATCH http://localhost:5005/management/buildings/REPLACE_WITH_BUILDING_ID/update/ \
  -H "Content-Type: application/json" \
  -d '{
    "address": "456 Updated Avenue",
    "metadata": {
      "floors": 12
    }
  }'
### Method: PATCH
>```
>{{base_url}}/management/buildings/:building_id/update/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "name": "3 Seasons Hotel",
    "type": "hotel",
    "address": "123 IoT Blvd",
    "metadata": {}
  }
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete
Generated from cURL: curl -X DELETE http://localhost:5005/management/buildings/REPLACE_WITH_BUILDING_ID/delete/
### Method: DELETE
>```
>{{base_url}}/management/buildings/:building_id/delete/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Detail
Generated from cURL: curl http://localhost:5005/management/buildings/REPLACE_WITH_BUILDING_ID/
### Method: GET
>```
>{{base_url}}/management/buildings/:building_id/
>```
### Response: 200
```json
{
    "id": "3f52bef7-001f-4844-a5fb-e209d769140a",
    "name": "3 Seasons Hotel",
    "type": "hotel",
    "address": "123 IoT Blvd",
    "metadata": {},
    "created_at": "2025-04-08T02:49:38.433279+00:00",
    "updated_at": "2025-04-08T02:49:38.433942+00:00"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Paginate
Generated from cURL: curl "http://localhost:5005/management/buildings/?page=1&per_page=5"
### Method: GET
>```
>{{base_url}}/management/buildings/?page=1&per_page=5
>```
### Query Params

|Param|value|
|---|---|
|page|1|
|per_page|5|


### Response: 200
```json
{
    "page": 1,
    "total_pages": 1,
    "total_items": 1,
    "has_next": false,
    "has_previous": false,
    "results": [
        {
            "id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "3 Seasons Hotel",
            "type": "hotel",
            "address": "123 IoT Blvd",
            "metadata": {},
            "created_at": "2025-04-08T02:49:38.433279+00:00",
            "updated_at": "2025-04-08T02:49:38.433942+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Devices detail
Generated from cURL: curl http://localhost:5005/management/buildings/REPLACE_WITH_BUILDING_ID/
### Method: GET
>```
>{{base_url}}/management/buildings/:building_id/devices/
>```
### Response: 200
```json
{
    "results": [
        {
            "id": "f8b315f5-195b-4ff4-b773-81542c739ede",
            "zone_id": null,
            "floor_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 1",
            "device_type": "energy",
            "serial_number": "PM-BLD-001",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:04:16.068616+00:00",
            "updated_at": "2025-04-08T03:04:16.068655+00:00"
        },
        {
            "id": "9d821104-e0ae-46c4-8eee-b9c041035425",
            "zone_id": null,
            "floor_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 2",
            "device_type": "energy",
            "serial_number": "PM-BLD-002",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:04:28.911606+00:00",
            "updated_at": "2025-04-08T03:04:28.911771+00:00"
        },
        {
            "id": "6c250940-9662-4378-ade9-cc6f2b813ba4",
            "zone_id": null,
            "floor_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 3",
            "device_type": "energy",
            "serial_number": "PM-BLD-003",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:04:54.673712+00:00",
            "updated_at": "2025-04-08T03:04:54.673815+00:00"
        },
        {
            "id": "6fb2ed4d-11bc-4dc5-8080-2df71346446a",
            "zone_id": null,
            "floor_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 4",
            "device_type": "energy",
            "serial_number": "PM-BLD-004",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:05:05.877487+00:00",
            "updated_at": "2025-04-08T03:05:05.877545+00:00"
        },
        {
            "id": "45cc791c-eec0-412c-9250-4bb1c425e343",
            "zone_id": null,
            "floor_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 5",
            "device_type": "energy",
            "serial_number": "PM-BLD-005",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:05:16.031502+00:00",
            "updated_at": "2025-04-08T03:05:16.031628+00:00"
        },
        {
            "id": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 101",
            "device_type": "iaq",
            "serial_number": "IAQ-ROOM-101",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T02:59:55.999898+00:00",
            "updated_at": "2025-04-08T02:59:56.000042+00:00"
        },
        {
            "id": "ec5c8170-c97a-483a-b2be-979f7a960780",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 101",
            "device_type": "presence",
            "serial_number": "PRESENCE-ROOM-101",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:02:07.290351+00:00",
            "updated_at": "2025-04-08T03:02:07.290535+00:00"
        },
        {
            "id": "52e1d349-844e-4167-8901-fdc46fd3e70a",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 102",
            "device_type": "presence",
            "serial_number": "PRESENCE-ROOM-102",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:02:34.359840+00:00",
            "updated_at": "2025-04-08T03:02:34.359953+00:00"
        },
        {
            "id": "86c68733-4da4-4d95-b0ba-26eed4880e98",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 102",
            "device_type": "iaq",
            "serial_number": "IAQ-ROOM-102",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:00:31.865103+00:00",
            "updated_at": "2025-04-08T03:00:31.865388+00:00"
        },
        {
            "id": "6f15fe69-e63c-451e-80e4-6bb647827666",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 103",
            "device_type": "presence",
            "serial_number": "PRESENCE-ROOM-103",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:03:04.152868+00:00",
            "updated_at": "2025-04-08T03:03:04.152973+00:00"
        },
        {
            "id": "1a064d86-6d2a-427a-8a9c-15f71df88853",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 103",
            "device_type": "iaq",
            "serial_number": "IAQ-ROOM-103",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:01:11.276316+00:00",
            "updated_at": "2025-04-08T03:01:11.276392+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Floors detail
Generated from cURL: curl http://localhost:5005/management/buildings/REPLACE_WITH_BUILDING_ID/
### Method: GET
>```
>{{base_url}}/management/buildings/:building_id/floors/
>```
### Response: 200
```json
{
    "results": [
        {
            "id": "9125d6d4-406d-4f71-9364-031345a52e3c",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "floor_number": 1,
            "name": "Ground Floor",
            "metadata": {
                "label": "L1",
                "has_elevator": false
            },
            "created_at": "2025-04-08T02:51:51.357974+00:00",
            "updated_at": "2025-04-08T02:51:51.358177+00:00"
        },
        {
            "id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "floor_number": 2,
            "name": "Second Floor",
            "metadata": {
                "label": "L2",
                "has_elevator": true
            },
            "created_at": "2025-04-08T02:51:27.037849+00:00",
            "updated_at": "2025-04-08T02:51:27.037909+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
## 📁 Collection: Floor 
undefined 


## End-point: Create
Generated from cURL: curl -X POST http://localhost:5005/management/floors/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "building_id": "REPLACE_WITH_BUILDING_ID",
    "floor_number": 2,
    "name": "Second Floor",
    "metadata": {
      "label": "L2",
      "has_elevator": true
    }
  }'
### Method: POST
>```
>{{base_url}}/management/floors/create/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
    "floor_number": 1,
    "name": "Ground Floor",
    "metadata": {
      "label": "L1",
      "has_elevator": false
    }
  }
```

### Response: 201
```json
{
    "id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468"
}
```

### Response: 201
```json
{
    "id": "9125d6d4-406d-4f71-9364-031345a52e3c"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update
Generated from cURL: curl -X PATCH http://localhost:5005/management/floors/REPLACE_WITH_FLOOR_ID/update/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Floor",
    "metadata": {
      "label": "UF2"
    }
  }'
### Method: PATCH
>```
>{{base_url}}/management/floors/:floor_id/update/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "name": "Updated Floor",
    "metadata": {
      "label": "UF2"
    }
  }
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete
Generated from cURL: curl -X DELETE http://localhost:5005/management/floors/REPLACE_WITH_FLOOR_ID/delete/
### Method: DELETE
>```
>{{base_url}}/management/floors/:floor_id/delete/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Detail
Generated from cURL: curl http://localhost:5005/management/floors/REPLACE_WITH_FLOOR_ID/
### Method: GET
>```
>{{base_url}}/management/floors/:floor_id/
>```
### Response: 200
```json
{
    "id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
    "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
    "floor_number": 2,
    "name": "Second Floor",
    "metadata": {
        "label": "L2",
        "has_elevator": true
    },
    "created_at": "2025-04-08T02:51:27.037849+00:00",
    "updated_at": "2025-04-08T02:51:27.037909+00:00"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Paginate
Generated from cURL: curl "http://localhost:5005/management/floors/?page=1&per_page=10"
### Method: GET
>```
>{{base_url}}/management/floors/?page=1&per_page=10
>```
### Query Params

|Param|value|
|---|---|
|page|1|
|per_page|10|


### Response: 200
```json
{
    "page": 1,
    "total_pages": 1,
    "total_items": 2,
    "has_next": false,
    "has_previous": false,
    "results": [
        {
            "id": "9125d6d4-406d-4f71-9364-031345a52e3c",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "floor_number": 1,
            "name": "Ground Floor",
            "metadata": {
                "label": "L1",
                "has_elevator": false
            },
            "created_at": "2025-04-08T02:51:51.357974+00:00",
            "updated_at": "2025-04-08T02:51:51.358177+00:00"
        },
        {
            "id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "floor_number": 2,
            "name": "Second Floor",
            "metadata": {
                "label": "L2",
                "has_elevator": true
            },
            "created_at": "2025-04-08T02:51:27.037849+00:00",
            "updated_at": "2025-04-08T02:51:27.037909+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Zones detail
Generated from cURL: curl http://localhost:5005/management/floors/REPLACE_WITH_FLOOR_ID/
### Method: GET
>```
>{{base_url}}/management/floors/:floor_id/zones/
>```
### Response: 200
```json
{
    "results": [
        {
            "id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "name": "Living Area",
            "metadata": {
                "has_ac": true
            },
            "created_at": "2025-04-08T02:54:22.340063+00:00",
            "updated_at": "2025-04-08T02:54:22.340155+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
## 📁 Collection: Zone 
undefined 


## End-point: Create
Generated from cURL: curl -X POST http://localhost:5005/management/zones/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "floor_id": "REPLACE_WITH_FLOOR_ID",
    "name": "Lobby Area",
    "metadata": {
      "has_ac": true,
      "camera_installed": false
    }
  }'
### Method: POST
>```
>{{base_url}}/management/zones/create/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "floor_id": "9125d6d4-406d-4f71-9364-031345a52e3c",
    "name": "Main Power",
    "metadata": {
      "has_ac": false
    }
  }
```

### Response: 201
```json
{
    "id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d"
}
```

### Response: 201
```json
{
    "id": "2b983d83-6940-4125-91cd-796fa758701c"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update
Generated from cURL: curl -X PATCH http://localhost:5005/management/zones/REPLACE_WITH_ZONE_ID/update/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Main Lobby",
    "metadata": {
      "has_ac": false
    }
  }'
### Method: PATCH
>```
>{{base_url}}/management/zones/:zone_id/update/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "name": "Main Lobby",
    "metadata": {
      "has_ac": false
    }
  }
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete
Generated from cURL: curl -X DELETE http://localhost:5005/management/zones/REPLACE_WITH_ZONE_ID/delete/
### Method: DELETE
>```
>{{base_url}}/management/zones/:zone_id/delete/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Detail
Generated from cURL: curl "http://localhost:5005/management/zones/?floor_id=REPLACE_WITH_FLOOR_ID"
### Method: GET
>```
>{{base_url}}/management/zones/:zone_id/
>```
### Response: 200
```json
{
    "id": "2b983d83-6940-4125-91cd-796fa758701c",
    "floor_id": "9125d6d4-406d-4f71-9364-031345a52e3c",
    "name": "Main Power",
    "metadata": {
        "has_ac": false
    },
    "created_at": "2025-04-08T02:54:44.996526+00:00",
    "updated_at": "2025-04-08T02:54:44.996641+00:00"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Paginate
Generated from cURL: curl "http://localhost:5005/management/zones/?page=1&per_page=10"
### Method: GET
>```
>{{base_url}}/management/zones/?page=1&per_page=10
>```
### Query Params

|Param|value|
|---|---|
|page|1|
|per_page|10|


### Response: 200
```json
{
    "page": 1,
    "total_pages": 1,
    "total_items": 2,
    "has_next": false,
    "has_previous": false,
    "results": [
        {
            "id": "2b983d83-6940-4125-91cd-796fa758701c",
            "floor_id": "9125d6d4-406d-4f71-9364-031345a52e3c",
            "name": "Main Power",
            "metadata": {
                "has_ac": false
            },
            "created_at": "2025-04-08T02:54:44.996526+00:00",
            "updated_at": "2025-04-08T02:54:44.996641+00:00"
        },
        {
            "id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "name": "Living Area",
            "metadata": {
                "has_ac": true
            },
            "created_at": "2025-04-08T02:54:22.340063+00:00",
            "updated_at": "2025-04-08T02:54:22.340155+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Devices detail
Generated from cURL: curl "http://localhost:5005/management/zones/?floor_id=REPLACE_WITH_FLOOR_ID"
### Method: GET
>```
>{{base_url}}/management/zones/:zone_id/devices/
>```
### Response: 200
```json
{
    "results": [
        {
            "id": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 101",
            "device_type": "iaq",
            "serial_number": "IAQ-ROOM-101",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T02:59:55.999898+00:00",
            "updated_at": "2025-04-08T02:59:56.000042+00:00"
        },
        {
            "id": "ec5c8170-c97a-483a-b2be-979f7a960780",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 101",
            "device_type": "presence",
            "serial_number": "PRESENCE-ROOM-101",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:02:07.290351+00:00",
            "updated_at": "2025-04-08T03:02:07.290535+00:00"
        },
        {
            "id": "86c68733-4da4-4d95-b0ba-26eed4880e98",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 102",
            "device_type": "iaq",
            "serial_number": "IAQ-ROOM-102",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:00:31.865103+00:00",
            "updated_at": "2025-04-08T03:00:31.865388+00:00"
        },
        {
            "id": "52e1d349-844e-4167-8901-fdc46fd3e70a",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 102",
            "device_type": "presence",
            "serial_number": "PRESENCE-ROOM-102",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:02:34.359840+00:00",
            "updated_at": "2025-04-08T03:02:34.359953+00:00"
        },
        {
            "id": "1a064d86-6d2a-427a-8a9c-15f71df88853",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 103",
            "device_type": "iaq",
            "serial_number": "IAQ-ROOM-103",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:01:11.276316+00:00",
            "updated_at": "2025-04-08T03:01:11.276392+00:00"
        },
        {
            "id": "6f15fe69-e63c-451e-80e4-6bb647827666",
            "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "floor_id": "5b9a7fcd-0fef-47fe-bda1-501f023c5468",
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Room 103",
            "device_type": "presence",
            "serial_number": "PRESENCE-ROOM-103",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "voltage_range": "220-240V"
            },
            "created_at": "2025-04-08T03:03:04.152868+00:00",
            "updated_at": "2025-04-08T03:03:04.152973+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
## 📁 Collection: Device 
undefined 


## End-point: Create under zone
Generated from cURL: curl -X POST http://localhost:5005/management/devices/create/ \
-H "Content-Type: application/json" \
-d '{
  "zone_id": "YOUR_ZONE_UUID",
  "name": "Power Meter Z1",
  "device_type": "power_meter",
  "serial_number": "PM-ZONE-001",
  "install_date": "2025-04-05T14:00:00Z",
  "metadata": {"voltage_range": "220-240V"}
}'
### Method: POST
>```
>{{base_url}}/management/devices/create/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "zone_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
    "name": "Room 103",
    "device_type": "presence",
    "serial_number": "PRESENCE-ROOM-103",
    "install_date": "2025-04-05T14:00:00Z",
    "metadata": {
        "voltage_range": "220-240V"
    }
}
```

### Response: 201
```json
{
    "id": "6c731696-ca4a-4167-9ac4-8bf31fec7e57"
}
```

### Response: 201
```json
{
    "id": "86c68733-4da4-4d95-b0ba-26eed4880e98"
}
```

### Response: 201
```json
{
    "id": "1a064d86-6d2a-427a-8a9c-15f71df88853"
}
```

### Response: 201
```json
{
    "id": "ec5c8170-c97a-483a-b2be-979f7a960780"
}
```

### Response: 201
```json
{
    "id": "52e1d349-844e-4167-8901-fdc46fd3e70a"
}
```

### Response: 201
```json
{
    "id": "6f15fe69-e63c-451e-80e4-6bb647827666"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create under building
Generated from cURL: curl -X POST http://localhost:5005/management/devices/create/ \
-H "Content-Type: application/json" \
-d '{
  "building_id": "YOUR_BUILDING_UUID",
  "name": "Main Power Meter",
  "device_type": "power_meter",
  "serial_number": "PM-BLD-001",
  "install_date": "2025-04-05T14:00:00Z",
  "metadata": {"location": "Main Switchboard"}
}'
### Method: POST
>```
>{{base_url}}/management/devices/create/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
    "name": "Power Meter 5",
    "device_type": "energy",
    "serial_number": "PM-UNIT-005",
    "install_date": "2025-04-05T14:00:00Z",
    "metadata": {
        "location": "Main Switchboard"
    }
}
```

### Response: 201
```json
{
    "id": "f8b315f5-195b-4ff4-b773-81542c739ede"
}
```

### Response: 201
```json
{
    "id": "9d821104-e0ae-46c4-8eee-b9c041035425"
}
```

### Response: 201
```json
{
    "id": "6c250940-9662-4378-ade9-cc6f2b813ba4"
}
```

### Response: 201
```json
{
    "id": "6fb2ed4d-11bc-4dc5-8080-2df71346446a"
}
```

### Response: 201
```json
{
    "id": "45cc791c-eec0-412c-9250-4bb1c425e343"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update
Generated from cURL: curl -X PATCH http://localhost:5005/management/devices/YOUR_DEVICE_UUID/update/ \
-H "Content-Type: application/json" \
-d '{"name": "Updated Name", "metadata": {"updated": true}}'
### Method: PATCH
>```
>{{base_url}}/management/devices/:device_id/update/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "name": "Updated Name",
    "metadata": {
        "updated": true
    }
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete
Generated from cURL: curl -X DELETE http://localhost:5005/management/devices/YOUR_DEVICE_UUID/delete/
### Method: DELETE
>```
>{{base_url}}/management/devices/:device_id/delete/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Detail
Generated from cURL: curl http://localhost:5005/management/devices/YOUR_DEVICE_UUID/
### Method: GET
>```
>{{base_url}}/management/devices/:device_id/
>```
### Response: 200
```json
{
    "id": "f8b315f5-195b-4ff4-b773-81542c739ede",
    "zone_id": null,
    "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
    "name": "Power Meter 1",
    "device_type": "energy",
    "serial_number": "PM-UNIT-001",
    "install_date": "2025-04-05T14:00:00+00:00",
    "metadata": {
        "location": "Main Switchboard"
    },
    "created_at": "2025-04-08T03:04:16.068616+00:00",
    "updated_at": "2025-04-08T03:04:16.068655+00:00"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Paginate
Generated from cURL: curl "http://localhost:5005/management/devices/?page=1&per_page=10&name=Power&device_type=power_meter"
### Method: GET
>```
>{{base_url}}/management/devices/?page=1&per_page=10&device_type=energy
>```
### Query Params

|Param|value|
|---|---|
|page|1|
|per_page|10|
|name||
|device_type|energy|


### Response: 200
```json
{
    "page": 1,
    "total_pages": 1,
    "total_items": 5,
    "has_next": false,
    "has_previous": false,
    "results": [
        {
            "id": "45cc791c-eec0-412c-9250-4bb1c425e343",
            "zone_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 5",
            "device_type": "energy",
            "serial_number": "PM-UNIT-005",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:05:16.031502+00:00",
            "updated_at": "2025-04-08T03:05:16.031628+00:00"
        },
        {
            "id": "6fb2ed4d-11bc-4dc5-8080-2df71346446a",
            "zone_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 4",
            "device_type": "energy",
            "serial_number": "PM-UNIT-004",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:05:05.877487+00:00",
            "updated_at": "2025-04-08T03:05:05.877545+00:00"
        },
        {
            "id": "6c250940-9662-4378-ade9-cc6f2b813ba4",
            "zone_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 3",
            "device_type": "energy",
            "serial_number": "PM-UNIT-003",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:04:54.673712+00:00",
            "updated_at": "2025-04-08T03:04:54.673815+00:00"
        },
        {
            "id": "9d821104-e0ae-46c4-8eee-b9c041035425",
            "zone_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 2",
            "device_type": "energy",
            "serial_number": "PM-UNIT-002",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:04:28.911606+00:00",
            "updated_at": "2025-04-08T03:04:28.911771+00:00"
        },
        {
            "id": "f8b315f5-195b-4ff4-b773-81542c739ede",
            "zone_id": null,
            "building_id": "3f52bef7-001f-4844-a5fb-e209d769140a",
            "name": "Power Meter 1",
            "device_type": "energy",
            "serial_number": "PM-UNIT-001",
            "install_date": "2025-04-05T14:00:00+00:00",
            "metadata": {
                "location": "Main Switchboard"
            },
            "created_at": "2025-04-08T03:04:16.068616+00:00",
            "updated_at": "2025-04-08T03:04:16.068655+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: PQs detail
Generated from cURL: curl http://localhost:5005/management/devices/YOUR_DEVICE_UUID/
### Method: GET
>```
>{{base_url}}/management/devices/:device_id/physical-quantities/
>```
### Response: 200
```json
{
    "results": [
        {
            "id": "8de8c92f-2bd7-4742-be85-11193dcc42ec",
            "device_id": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
            "datapoint": "co2",
            "unit": "ppm",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:10:54.814598+00:00",
            "updated_at": "2025-04-08T03:10:54.814614+00:00"
        },
        {
            "id": "b97cf5e0-f9a7-4077-8a41-c44571779886",
            "device_id": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
            "datapoint": "humidity",
            "unit": "%RH",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:10:54.814532+00:00",
            "updated_at": "2025-04-08T03:10:54.814548+00:00"
        },
        {
            "id": "1f8886cf-1248-49f1-8430-0548cc59feae",
            "device_id": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
            "datapoint": "temperature",
            "unit": "°C",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:10:54.814345+00:00",
            "updated_at": "2025-04-08T03:10:54.814473+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
## 📁 Collection: PhysicalQuantity 
undefined 


## End-point: Create
Generated from cURL: curl -X POST http://localhost:5005/management/physical-quantities/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "device_id": "REPLACE_WITH_DEVICE_ID",
    "datapoint": "temperature",
    "unit": "°C",
    "formula": "raw * 0.1",
    "metadata": {
      "sensor_port": "A0"
    }
  }'
### Method: POST
>```
>{{base_url}}/management/physical-quantities/create/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "device_id": "REPLACE_WITH_DEVICE_ID",
    "datapoint": "temperature",
    "unit": "°C",
    "formula": "raw * 0.1",
    "metadata": {
      "sensor_port": "A0"
    }
  }
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create many
Generated from cURL: curl -X POST http://localhost:5005/management/physical-quantities/bulk/ \
  -H "Content-Type: application/json" \
  -d '[
    {
      "device_id": "REPLACE_WITH_DEVICE_ID",
      "datapoint": "temperature",
      "unit": "°C",
      "formula": "raw * 0.1"
    },
    {
      "device_id": "REPLACE_WITH_DEVICE_ID",
      "datapoint": "humidity",
      "unit": "%",
      "formula": "raw * 0.5"
    }
  ]'
### Method: POST
>```
>{{base_url}}/management/physical-quantities/bulk/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
[
    {
      "device_id": "f8b315f5-195b-4ff4-b773-81542c739ede",
      "datapoint": "power",
      "unit": "kW",
      "formula": "x"
    },
    {
      "device_id": "9d821104-e0ae-46c4-8eee-b9c041035425",
      "datapoint": "power",
      "unit": "kW",
      "formula": "x"
    },
    {
      "device_id": "6c250940-9662-4378-ade9-cc6f2b813ba4",
      "datapoint": "power",
      "unit": "kW",
      "formula": "x"
    },
    {
      "device_id": "6fb2ed4d-11bc-4dc5-8080-2df71346446a",
      "datapoint": "power",
      "unit": "kW",
      "formula": "x"
    },
    {
      "device_id": "45cc791c-eec0-412c-9250-4bb1c425e343",
      "datapoint": "power",
      "unit": "kW",
      "formula": "x"
    }
  ]
```

### Response: 201
```json
{
    "created": 3
}
```

### Response: 201
```json
{
    "created": 3
}
```

### Response: 201
```json
{
    "created": 3
}
```

### Response: 201
```json
{
    "created": 3
}
```

### Response: 201
```json
{
    "created": 3
}
```

### Response: 201
```json
{
    "created": 3
}
```

### Response: 201
```json
{
    "created": 5
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update
Generated from cURL: curl -X PATCH http://localhost:5005/management/physical-quantities/REPLACE_WITH_ID/update/ \
  -H "Content-Type: application/json" \
  -d '{
    "unit": "Kelvin",
    "formula": "raw * 1.0 + 273.15"
  }'
### Method: PATCH
>```
>{{base_url}}/management/physical-quantities/:physical_quantity_id/update/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "unit": "Kelvin",
    "formula": "raw * 1.0 + 273.15"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete
Generated from cURL: curl -X DELETE http://localhost:5005/management/physical-quantities/REPLACE_WITH_ID/delete/
### Method: DELETE
>```
>{{base_url}}/management/physical-quantities/:physical_quantity_id/delete/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Detail
Generated from cURL: curl http://localhost:5005/management/physical-quantities/REPLACE_WITH_ID/
### Method: GET
>```
>{{base_url}}/management/physical-quantities/:physical_quantity_id/
>```
### Response: 200
```json
{
    "id": "1f8886cf-1248-49f1-8430-0548cc59feae",
    "device_id": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
    "datapoint": "temperature",
    "unit": "°C",
    "formula": "x",
    "metadata": {},
    "created_at": "2025-04-08T03:10:54.814345+00:00",
    "updated_at": "2025-04-08T03:10:54.814473+00:00"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Paginate
Generated from cURL: curl "http://localhost:5005/management/physical-quantities/?page=1&per_page=10"
### Method: GET
>```
>{{base_url}}/management/physical-quantities/?page=1&per_page=10
>```
### Query Params

|Param|value|
|---|---|
|page|1|
|per_page|10|


### Response: 200
```json
{
    "page": 1,
    "total_pages": 3,
    "total_items": 23,
    "has_next": true,
    "has_previous": false,
    "results": [
        {
            "id": "ecf1606d-5834-457a-8281-ec63a40575a7",
            "device_id": "45cc791c-eec0-412c-9250-4bb1c425e343",
            "datapoint": "power",
            "unit": "kW",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:49.558787+00:00",
            "updated_at": "2025-04-08T03:11:49.558801+00:00"
        },
        {
            "id": "8f05cabf-dcfc-4e82-bbf1-b70a9f5f7225",
            "device_id": "6fb2ed4d-11bc-4dc5-8080-2df71346446a",
            "datapoint": "power",
            "unit": "kW",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:49.558722+00:00",
            "updated_at": "2025-04-08T03:11:49.558737+00:00"
        },
        {
            "id": "29de22dc-4422-4528-823e-77eb2c5a2e41",
            "device_id": "6c250940-9662-4378-ade9-cc6f2b813ba4",
            "datapoint": "power",
            "unit": "kW",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:49.558648+00:00",
            "updated_at": "2025-04-08T03:11:49.558669+00:00"
        },
        {
            "id": "3af475eb-1b3f-41e0-9b74-db1555364360",
            "device_id": "9d821104-e0ae-46c4-8eee-b9c041035425",
            "datapoint": "power",
            "unit": "kW",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:49.558504+00:00",
            "updated_at": "2025-04-08T03:11:49.558537+00:00"
        },
        {
            "id": "95e06b8d-9120-46f4-85ad-1ca663b87f27",
            "device_id": "f8b315f5-195b-4ff4-b773-81542c739ede",
            "datapoint": "power",
            "unit": "kW",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:49.558234+00:00",
            "updated_at": "2025-04-08T03:11:49.558372+00:00"
        },
        {
            "id": "cf5c3ab7-8d02-48a5-8810-ecad27daec57",
            "device_id": "6f15fe69-e63c-451e-80e4-6bb647827666",
            "datapoint": "presence_state",
            "unit": "state",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:33.878931+00:00",
            "updated_at": "2025-04-08T03:11:33.878949+00:00"
        },
        {
            "id": "77449183-dcc6-4266-a62a-b095b2c6e79f",
            "device_id": "6f15fe69-e63c-451e-80e4-6bb647827666",
            "datapoint": "sensitivity",
            "unit": "%",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:33.878857+00:00",
            "updated_at": "2025-04-08T03:11:33.878874+00:00"
        },
        {
            "id": "cf3b5b97-24d5-449e-a093-b950d4e23342",
            "device_id": "6f15fe69-e63c-451e-80e4-6bb647827666",
            "datapoint": "online_status",
            "unit": "status",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:33.878664+00:00",
            "updated_at": "2025-04-08T03:11:33.878795+00:00"
        },
        {
            "id": "97c064b9-367c-4cbd-b9ac-a3e3d506611d",
            "device_id": "52e1d349-844e-4167-8901-fdc46fd3e70a",
            "datapoint": "presence_state",
            "unit": "state",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:26.376069+00:00",
            "updated_at": "2025-04-08T03:11:26.376083+00:00"
        },
        {
            "id": "cf06b46a-492a-4c6d-8614-8275c5215420",
            "device_id": "52e1d349-844e-4167-8901-fdc46fd3e70a",
            "datapoint": "sensitivity",
            "unit": "%",
            "formula": "x",
            "metadata": {},
            "created_at": "2025-04-08T03:11:26.376005+00:00",
            "updated_at": "2025-04-08T03:11:26.376020+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: Fault Detection 
Manage alert configs, trigger alerts, and handle acknowledgements. 


## End-point: Alert disconnection device
### Method: POST
>```
>{{base_url}}/fault-detection/cron/devices/disconnect-alerts/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Buildings detail
### Method: GET
>```
>{{base_url}}/fault-detection/alert/:building_id/buildings/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Floors detail
### Method: GET
>```
>{{base_url}}/fault-detection/alert/:building_id/floors/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Zones detail
### Method: GET
>```
>{{base_url}}/fault-detection/alert/:building_id/zones/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Devices detail
### Method: GET
>```
>{{base_url}}/fault-detection/alert/:building_id/devices/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create
Generated from cURL: curl -X POST http://localhost:8000/fault-configs/create/ \
  -H "Content-Type: application/json" \
  -d '{
        "target_type": "room",
        "target_id": "room101",
        "datapoint": "temperature",
        "aggregation": "avg",
        "min_value": 18,
        "max_value": 28,
        "logic_expression": "x < 18 or x > 28",
        "priority": 5,
        "enabled": true
      }'
### Method: POST
>```
>{{base_url}}/fault-detection/configs/create/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
    "target_type": "device",
    "target_id": "45cc791c-eec0-412c-9250-4bb1c425e343",
    "datapoint": "power",
    "aggregation": "none",
    "min_value": 0,
    "max_value": 5,
    "logic_expression": "x > 5",
    "priority": 5,
    "enabled": true,
    "alert_repeat_interval_minutes": 5,
    "alert_data_silence_threshold_minutes": 1
}
```

### Response: 201
```json
{
    "id": "c9227b24-cbc1-4b8b-a3a9-67ada3161781"
}
```

### Response: 201
```json
{
    "id": "b08ebda8-ab60-4e91-9bde-616358cd5fda"
}
```

### Response: 201
```json
{
    "id": "96455ed0-1080-4bad-a02e-6ad23079f0f3"
}
```

### Response: 201
```json
{
    "id": "5a95991f-1752-43dd-b87c-ac25634c37cb"
}
```

### Response: 201
```json
{
    "id": "9af578ab-1e76-4a58-986e-a22cbffae01c"
}
```

### Response: 201
```json
{
    "id": "cc2e5503-c803-4174-bc63-a3e6412f44bb"
}
```

### Response: 201
```json
{
    "id": "2f1a0135-aef0-40f5-a06d-693aa544ee7e"
}
```

### Response: 201
```json
{
    "id": "65d107e5-a7f7-4086-9c2d-a839c64375da"
}
```

### Response: 201
```json
{
    "id": "9dfd6186-32fa-4f2b-92aa-f0778164fa70"
}
```

### Response: 201
```json
{
    "id": "c90f80eb-33d8-4063-a91a-bbcace3714a0"
}
```

### Response: 201
```json
{
    "id": "e64b4585-a238-4382-b173-54bf9f9a68e3"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Update
Generated from cURL: curl -X PATCH http://localhost:8000/fault-configs/<CONFIG_ID>/update/ \
  -H "Content-Type: application/json" \
  -d '{
        "max_value": 30,
        "logic_expression": "x < 18 or x > 30"
      }'
### Method: PATCH
>```
>{{base_url}}/fault-detection/configs/:config_id/update/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
        "max_value": 30,
        "logic_expression": "x < 18 or x > 30"
      }
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Delete
Generated from cURL: curl -X DELETE http://localhost:8000/fault-configs/<CONFIG_ID>/delete/
### Method: DELETE
>```
>{{base_url}}/fault-detection/configs/:config_id/delete/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Detail
Generated from cURL: curl http://localhost:8000/fault-configs/<CONFIG_ID>/
### Method: GET
>```
>{{base_url}}/fault-detection/configs/:config_id/
>```
### Response: 200
```json
{
    "id": "c9227b24-cbc1-4b8b-a3a9-67ada3161781",
    "target_type": "device",
    "target_id": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
    "datapoint": "temperature",
    "aggregation": "none",
    "min_value": 20,
    "max_value": 26,
    "logic_expression": "x < 20 or x > 26 or (x > 24 and time_hour >= 0 and time_hour < 6)",
    "priority": 4,
    "enabled": true,
    "alert_repeat_interval_minutes": 5,
    "alert_data_silence_threshold_minutes": 1,
    "created_at": "2025-04-08T04:10:55.734956+00:00",
    "updated_at": "2025-04-08T04:10:55.736055+00:00"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Paginate
Generated from cURL: curl "http://localhost:8000/fault-configs/?page=1&per_page=10"
### Method: GET
>```
>{{base_url}}/fault-detection/configs/?page=1&per_page=10
>```
### Query Params

|Param|value|
|---|---|
|page|1|
|per_page|10|


### Response: 200
```json
{
    "page": 1,
    "total_pages": 2,
    "total_items": 11,
    "has_next": true,
    "has_previous": false,
    "results": [
        {
            "id": "e64b4585-a238-4382-b173-54bf9f9a68e3",
            "target_type": "device",
            "target_id": "45cc791c-eec0-412c-9250-4bb1c425e343",
            "datapoint": "power",
            "aggregation": "none",
            "min_value": 0,
            "max_value": 5,
            "logic_expression": "x > 5",
            "priority": 5,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:23:34.850412+00:00",
            "updated_at": "2025-04-08T04:23:34.850702+00:00"
        },
        {
            "id": "c90f80eb-33d8-4063-a91a-bbcace3714a0",
            "target_type": "device",
            "target_id": "6fb2ed4d-11bc-4dc5-8080-2df71346446a",
            "datapoint": "power",
            "aggregation": "none",
            "min_value": 0,
            "max_value": 5,
            "logic_expression": "x > 5",
            "priority": 5,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:23:19.072643+00:00",
            "updated_at": "2025-04-08T04:23:19.072817+00:00"
        },
        {
            "id": "9dfd6186-32fa-4f2b-92aa-f0778164fa70",
            "target_type": "device",
            "target_id": "6c250940-9662-4378-ade9-cc6f2b813ba4",
            "datapoint": "power",
            "aggregation": "none",
            "min_value": 0,
            "max_value": 5,
            "logic_expression": "x > 5",
            "priority": 5,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:22:47.045143+00:00",
            "updated_at": "2025-04-08T04:22:47.045243+00:00"
        },
        {
            "id": "65d107e5-a7f7-4086-9c2d-a839c64375da",
            "target_type": "device",
            "target_id": "9d821104-e0ae-46c4-8eee-b9c041035425",
            "datapoint": "power",
            "aggregation": "none",
            "min_value": 0,
            "max_value": 5,
            "logic_expression": "x > 5",
            "priority": 5,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:22:28.358762+00:00",
            "updated_at": "2025-04-08T04:22:28.358938+00:00"
        },
        {
            "id": "2f1a0135-aef0-40f5-a06d-693aa544ee7e",
            "target_type": "device",
            "target_id": "f8b315f5-195b-4ff4-b773-81542c739ede",
            "datapoint": "power",
            "aggregation": "none",
            "min_value": 0,
            "max_value": 5,
            "logic_expression": "x > 5",
            "priority": 5,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:21:37.729520+00:00",
            "updated_at": "2025-04-08T04:21:37.730019+00:00"
        },
        {
            "id": "cc2e5503-c803-4174-bc63-a3e6412f44bb",
            "target_type": "device",
            "target_id": "1a064d86-6d2a-427a-8a9c-15f71df88853",
            "datapoint": "humidity",
            "aggregation": "none",
            "min_value": 30,
            "max_value": 60,
            "logic_expression": "x < 30 or x > 65 or (x > 60 and temperature > 27)",
            "priority": 4,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:16:27.927740+00:00",
            "updated_at": "2025-04-08T04:16:27.927849+00:00"
        },
        {
            "id": "9af578ab-1e76-4a58-986e-a22cbffae01c",
            "target_type": "device",
            "target_id": "86c68733-4da4-4d95-b0ba-26eed4880e98",
            "datapoint": "humidity",
            "aggregation": "none",
            "min_value": 30,
            "max_value": 60,
            "logic_expression": "x < 30 or x > 65 or (x > 60 and temperature > 27)",
            "priority": 4,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:16:00.711050+00:00",
            "updated_at": "2025-04-08T04:16:00.711682+00:00"
        },
        {
            "id": "5a95991f-1752-43dd-b87c-ac25634c37cb",
            "target_type": "device",
            "target_id": "6c731696-ca4a-4167-9ac4-8bf31fec7e57",
            "datapoint": "humidity",
            "aggregation": "none",
            "min_value": 30,
            "max_value": 60,
            "logic_expression": "x < 30 or x > 65 or (x > 60 and temperature > 27)",
            "priority": 4,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:15:27.872505+00:00",
            "updated_at": "2025-04-08T04:15:27.872917+00:00"
        },
        {
            "id": "96455ed0-1080-4bad-a02e-6ad23079f0f3",
            "target_type": "device",
            "target_id": "6f15fe69-e63c-451e-80e4-6bb647827666",
            "datapoint": "temperature",
            "aggregation": "none",
            "min_value": 20,
            "max_value": 26,
            "logic_expression": "x < 20 or x > 26 or (x > 24 and time_hour >= 0 and time_hour < 6)",
            "priority": 4,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:12:03.076987+00:00",
            "updated_at": "2025-04-08T04:12:03.077084+00:00"
        },
        {
            "id": "b08ebda8-ab60-4e91-9bde-616358cd5fda",
            "target_type": "device",
            "target_id": "f685ccbe-2cbe-4607-b99c-09b4d90b746d",
            "datapoint": "temperature",
            "aggregation": "none",
            "min_value": 20,
            "max_value": 26,
            "logic_expression": "x < 20 or x > 26 or (x > 24 and time_hour >= 0 and time_hour < 6)",
            "priority": 4,
            "enabled": true,
            "alert_repeat_interval_minutes": 5,
            "alert_data_silence_threshold_minutes": 1,
            "created_at": "2025-04-08T04:11:44.880173+00:00",
            "updated_at": "2025-04-08T04:11:44.880300+00:00"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Acknowledge
Generated from cURL: curl -X POST http://localhost:8000/fault-alert/9fbd1c14-1c74-4a1e-a443-e82b77239e49/acknowledge/ \
  -H "Content-Type: application/json" \
  -d '{
        "acknowledged_by": "john.doe@example.com",
        "acknowledge_older": true
      }'
### Method: PATCH
>```
>{{base_url}}/fault-detection/alert/:alert_id/acknowledge/
>```
### Headers

|Content-Type|Value|
|---|---|
|Content-Type|application/json|


### Body (**raw**)

```json
{
        "acknowledged_by": "xyz@example.com",
        "acknowledge_older": true
      }
```

### Response: 200
```json
{
    "acknowledged_count": 1,
    "acknowledged_alert_ids": [
        "68d613e8-21b2-401b-904f-9bf8d9932166"
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
