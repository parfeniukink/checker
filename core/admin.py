from django.contrib import admin

from core.models import Report, ReportStatuses, Website


class ReportInline(admin.TabularInline):
    model = Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_display = ("site", "status", "created_at", "available")
    search_fields = ["site", "status", "created_at"]

    @admin.display(boolean=True, ordering="-status")
    def available(self, obj):
        return obj.status == ReportStatuses.AVAILABLE.value


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    inlines = [ReportInline]

    exclude = ("id",)
