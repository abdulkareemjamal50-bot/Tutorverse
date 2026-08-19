from django.contrib import admin
from .models import Category, Subject


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'education_level',
    )

    list_filter = (
        'education_level',
    )

    search_fields = (
        'name',
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
    )

    list_filter = (
        'category',
        'category__education_level',
    )

    search_fields = (
        'name',
    )