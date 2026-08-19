from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'teacher',
        'subject',
        'lesson_date',
        'lesson_time',
        'status'
    )

    list_filter = (
        'status',
        'is_online',
    )

    search_fields = (
        'student__username',
        'teacher__user__username',
        'subject',
    )
