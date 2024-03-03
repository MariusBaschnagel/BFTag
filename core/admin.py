from django.contrib import admin
from . import models


class FahrzeugModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname')


class LogMessageModelAdmin(admin.ModelAdmin):
    list_display = ('stichwort', 'adresse', 'fahrzeuge', 'timestamp')
    list_filter = ('timestamp', 'stichwort')


admin.site.register(models.Fahrzeug, FahrzeugModelAdmin)
admin.site.register(models.Logmessage, LogMessageModelAdmin)
