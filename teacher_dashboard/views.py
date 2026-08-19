from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from bookings.models import Booking
from courses.models import Course


@login_required
def dashboard(request):

    bookings = Booking.objects.filter(
        teacher__user=request.user
    ).order_by('-booked_at')

    pending_bookings = bookings.filter(
        status='pending'
    )

    accepted_bookings = bookings.filter(
        status='accepted'
    )

    completed_bookings = bookings.filter(
        status='completed'
    )

    courses = Course.objects.filter(
        teacher__user=request.user
    ).order_by('-created_at')

    context = {
        'bookings': bookings,
        'pending_bookings': pending_bookings,
        'accepted_bookings': accepted_bookings,
        'completed_bookings': completed_bookings,
        'courses': courses,
    }

    return render(
        request,
        'teacher_dashboard/dashboard.html',
        context
    )


@login_required
def teacher_courses(request):

    courses = Course.objects.filter(
        teacher__user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'teacher_dashboard/teacher_courses.html',
        {
            'courses': courses
        }
    )