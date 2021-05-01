from django.contrib import admin
from django.contrib.admin import register

from tasks.models import Task


@register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
