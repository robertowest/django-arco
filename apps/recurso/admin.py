from django.contrib import admin
from . import models

@admin.register(models.Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = models.Grupo.list_display
    list_display_links = models.Grupo.list_display_links
    search_fields = models.Grupo.search_fields

    # def get_ordering(self, request):
        # return [self.nombre.lower()]


@admin.register(models.Subgrupo)
class SubgrupoAdmin(admin.ModelAdmin):
    list_display = models.Subgrupo.list_display
    list_display_links = models.Subgrupo.list_display_links
    search_fields = models.Subgrupo.search_fields
    list_filter = models.Subgrupo.list_filter


@admin.register(models.Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = models.Recurso.list_display
    list_display_links = models.Recurso.list_display_links
    search_fields = models.Recurso.search_fields
    list_filter = models.Recurso.list_filter
