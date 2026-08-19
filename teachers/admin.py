from django.contrib import admin
from .models import TeacherProfile


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'qualification',
        'experience',
        'hourly_rate',
        'lesson_mode',
        'city',
        'state',
        'verified',
        'is_available',
    )

    list_filter = (
        'lesson_mode',
        'verified',
        'is_available',
        'state',
    )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'city',
        'state',
    )

    filter_horizontal = (
        'subjects',
    )