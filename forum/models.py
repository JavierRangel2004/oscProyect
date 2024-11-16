# forum/admin.py

from django.contrib import admin
from .models import Forum, Post, Comment

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ('name', 'description', 'created_by__username')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'created_by', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'content', 'forum__name', 'created_by__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created_by', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('content', 'post__title', 'created_by__username')
