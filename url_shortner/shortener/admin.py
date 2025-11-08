from django.contrib import admin
from .models import URL

class URLAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'original_url', 'clicks')  # match model fields

admin.site.register(URL, URLAdmin)
