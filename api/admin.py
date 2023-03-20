from django.contrib import admin

from api.models import ShortLink


@admin.register(ShortLink)
class ShortLinkModel(admin.ModelAdmin):
    list_display = ('short_url', 'full_url', 'created_date', 'request_count', 'is_active')
    search_fields = ('full_url', 'short_url',)
    ordering = ('-created_date',)

