from django.contrib import admin
from .models import URL

# Register your models here.
@admin.register(URL)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['long_url', 'short_url', 'clicks']
    ordering = ['-clicks']