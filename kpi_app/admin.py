from django.contrib import admin
from .models import Circle, Kpi
from simple_history.admin import SimpleHistoryAdmin


SimpleHistoryAdmin.enforce_history_permissions = True


class CircleAdmin(SimpleHistoryAdmin):
    list_display = ("circle_name",)


class KpiAdmin(SimpleHistoryAdmin):

    def get_circ(self, obj):
        return [c.circle_name for c in obj.circle.all()]
    
    get_circ.short_description = "Circle(s)"

    list_display = ("kpi_name", "get_circ", "value", "year", "month", "created_at", "updated_at", "updated_by")
    history_list_display = ["value", "year", "month"]



admin.site.register(Circle, CircleAdmin)
admin.site.register(Kpi, KpiAdmin)

