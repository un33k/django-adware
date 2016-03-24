from .models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "percentage",
        "ad_client",
        "ad_slot",
        "is_active",
        "updated_at",
    ]
admin.site.register(Ad, AdAdmin)
