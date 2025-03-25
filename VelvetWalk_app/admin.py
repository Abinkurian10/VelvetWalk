from django.contrib import admin
from .models import Profile, BlogPost, Comment

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'website']
    search_fields = ['user__username', 'bio']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at', 'views']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'content', 'author__username']
    date_hierarchy = 'created_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'author__username', 'post__title']
    date_hierarchy = 'created_at' 