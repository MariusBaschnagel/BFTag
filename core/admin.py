from django.contrib import admin
from . import models


class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ("name", "shortname")


class OperationModelAdmin(admin.ModelAdmin):
    list_display = ("keyword", "address", "vehicles", "dispatched")
    list_filter = ("dispatched", "keyword")


admin.site.register(models.Vehicle, VehicleModelAdmin)
admin.site.register(models.Operation, OperationModelAdmin)
