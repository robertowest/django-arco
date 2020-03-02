from django.contrib import admin

# Register your models here.
from . import models


class SectionsAdmin(admin.ModelAdmin):
    list_display = ['section', 'label', 'ordered', 'active']
    ordering = ['section', 'ordered']

    list_filter = ['section', 'active']
    search_fields = ['label']
    list_per_page = 20

admin.site.register(models.Sections, SectionsAdmin)