from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'author',
        'published',
        'created_at',
    )

    list_filter = (
        'category',
        'published',
        'created_at',
    )

    search_fields = (
        'title',
        'content',
        'author',
    )

    prepopulated_fields = {
        'slug': ('title',)
    }