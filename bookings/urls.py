from django.urls import path
from . import views

urlpatterns = [

    # Student creates booking
    path(
        'book/<int:teacher_id>/',
        views.create_booking,
        name='create_booking'
    ),

    # Booking success
    path(
        'booking-success/',
        views.booking_success,
        name='booking_success'
    ),

    # Student's bookings
    path(
        'my-bookings/',
        views.my_bookings,
        name='my_bookings'
    ),

    # Student views one booking
    path(
        'my-bookings/<int:booking_id>/',
        views.student_booking_detail,
        name='student_booking_detail'
    ),

    # Teacher views one booking
    path(
        'teacher-booking/<int:booking_id>/',
        views.booking_detail,
        name='booking_detail'
    ),

    # Teacher accepts/cancels booking
    path(
        'teacher-booking/<int:booking_id>/update/',
        views.update_booking_status,
        name='update_booking_status'
    ),
]