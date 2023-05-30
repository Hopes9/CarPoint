from django.contrib import admin
from findCar.models import State, County, Location, Car, Cargo


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        "state_id",
        "state_name"
    ]


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = [
        "county_fips",
        "county_name",
        "location",
    ]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_select_related = ('state',)
    list_display = [
        "zip",
        "lat",
        "lng",
        "city",
        "state",
    ]


@admin.register(Car)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "number",
        "current_location",
        "carrying_capacity",

    ]


@admin.register(Cargo)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "pickup_lat",
        "pickup_lng",
        "zipCode",
        "weight",
    ]
