from django.contrib import admin
from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'school',
        'level',
        'city',
        'state',
        'joined_at',
    )

    list_filter = (
        'state',
        'level',
    )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'school',
        'city',
        'state',
    )