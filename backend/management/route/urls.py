from django.urls import path

from .api.handler import (
    hand_building,
    hand_device,
    hand_floor,
    hand_physical_quantity,
    hand_zone,
)

urlpatterns = [
    # Building
    path("buildings/", hand_building.list_items),
    path("buildings/create/", hand_building.create),
    path("buildings/<uuid:building_id>/", hand_building.detail),
    path("buildings/<uuid:building_id>/update/", hand_building.update),
    path("buildings/<uuid:building_id>/delete/", hand_building.delete),
    path("buildings/<uuid:building_id>/floors/", hand_floor.list_by_building),
    path("buildings/<uuid:building_id>/devices/", hand_device.list_by_building),
    # Floor
    path("floors/", hand_floor.list_items),
    path("floors/create/", hand_floor.create),
    path("floors/<uuid:floor_id>/", hand_floor.detail),
    path("floors/<uuid:floor_id>/update/", hand_floor.update),
    path("floors/<uuid:floor_id>/delete/", hand_floor.delete),
    path("floors/<uuid:floor_id>/zones/", hand_zone.list_by_floor),
    path("floors/<uuid:floor_id>/devices/", hand_device.list_by_floor),
    # Zone
    path("zones/", hand_zone.list_items),
    path("zones/create/", hand_zone.create),
    path("zones/<uuid:zone_id>/", hand_zone.detail),
    path("zones/<uuid:zone_id>/update/", hand_zone.update),
    path("zones/<uuid:zone_id>/delete/", hand_zone.delete),
    path("zones/<uuid:zone_id>/devices/", hand_device.list_by_zone),
    # Device
    path("devices/", hand_device.list_items),
    path("devices/create/", hand_device.create),
    path("devices/<uuid:device_id>/", hand_device.detail),
    path("devices/<uuid:device_id>/update/", hand_device.update),
    path("devices/<uuid:device_id>/delete/", hand_device.delete),
    path("devices/<uuid:device_id>/physical-quantities/", hand_physical_quantity.list_by_device),
    # Physical Quantity
    path("physical-quantities/", hand_physical_quantity.list_items),
    path("physical-quantities/create/", hand_physical_quantity.create),
    path("physical-quantities/bulk/", hand_physical_quantity.create_many),
    path("physical-quantities/<uuid:physical_quantity_id>/", hand_physical_quantity.detail),
    path("physical-quantities/<uuid:physical_quantity_id>/update/", hand_physical_quantity.update),
    path("physical-quantities/<uuid:physical_quantity_id>/delete/", hand_physical_quantity.delete),
]
