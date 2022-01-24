from django.contrib import admin
from .models import Project
from .models import Task

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    list_display = ['name', 'user', ]
    list_filter = ['name', 'user', ]
    search_fields = ['name', 'user', 'status',]
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model = Project

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name','project']
    list_filter = ['project', ]
    search_fields = ['project']


# admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)