from django.contrib import admin

from webapp.models import Project


class ProjectAdimin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'create_add']
    list_filter = ['description', 'status']
    search_fields = ['description', 'status']
    fields = ['id', 'description', 'status', 'create_add']




admin.site.register(Project,ProjectAdimin )

