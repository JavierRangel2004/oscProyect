# forum/admin.py

from django.contrib import admin
from .models import Forum, Post, Comment

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    search_fields = ('name', 'description', 'created_by__username')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'created_by', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at', 'forum')
    search_fields = ('title', 'content', 'created_by__username', 'forum__name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created_by', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('content', 'created_by__username', 'post__title')
