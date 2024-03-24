from django.contrib import admin
from .models import URL

# Register your models here.
@admin.register(URL)
class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'short', 'visits']
    ordering = ['-visits']