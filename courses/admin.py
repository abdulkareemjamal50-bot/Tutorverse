from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'teacher',
        'category',
        'subject',
        'education_level',
        'price',
        'is_available',
    )

    list_filter = (
        'category',
        'subject',
        'education_level',
        'is_available',
    )

    search_fields = (
        'title',
        'teacher__user__username',
        'teacher__user__first_name',
        'teacher__user__last_name',
    )
