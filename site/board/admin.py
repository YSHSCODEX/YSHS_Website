from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    list_per_page = 10

    