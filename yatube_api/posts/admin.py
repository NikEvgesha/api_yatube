from django.contrib import admin

from posts.models import Comment, Group, Post


@admin.register(Post, Group, Comment)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('text',)
    empty_value_display = '-пусто-'
