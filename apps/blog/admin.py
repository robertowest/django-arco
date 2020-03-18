from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = models.Post.list_display
    list_display_links = models.Post.list_display_links
    exclude = models.Post.exclude
    search_fields = models.Post.search_fields
    list_filter = models.Post.list_filter
    date_hierarchy = models.Post.date_hierarchy
