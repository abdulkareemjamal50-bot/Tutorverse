from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from bookings.models import Booking


@login_required
def dashboard(request):

    bookings = Booking.objects.filter(
        student=request.user
    ).order_by('-booked_at')

    pending_bookings = bookings.filter(
        status='pending'
    )

    accepted_bookings = bookings.filter(
        status='accepted'
    )

    context = {
        'bookings': bookings,
        'pending_bookings': pending_bookings,
        'accepted_bookings': accepted_bookings,
    }

    return render(
        request,
        'student_dashboard/dashboard.html',
        context
    )