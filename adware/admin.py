from django.contrib import admin

from .models import AdSense


class AdSenseAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "percentage",
        "ad_client",
        "ad_slot",
        "is_active",
        "updated_at",
    ]
admin.site.register(AdSense, AdSenseAdmin)
