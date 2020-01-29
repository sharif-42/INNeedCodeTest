from django.contrib import admin

from .models import UserFile


@admin.register(UserFile)
class UserFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file', 'created_at')
    list_filter = ('user', 'created_at')
    date_hierarchy = 'created_at'
