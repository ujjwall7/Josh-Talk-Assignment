from django.contrib import admin
from .models import *

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'email', 'mobile', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'name', 'mobile')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task_type', 'status', 'created_at', 'completed_at')
    list_filter = ('status', 'task_type', 'created_at')
    search_fields = ('name', 'description')
    filter_horizontal = ('assigned_users',)
