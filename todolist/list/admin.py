from django.contrib import admin

from .models import *


class TasksAdmin(admin.ModelAdmin):
    list_display = ("title", "create_date")


admin.site.register(Tasks, TasksAdmin)
