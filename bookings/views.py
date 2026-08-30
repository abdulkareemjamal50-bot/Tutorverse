from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from teachers.models import TeacherProfile
from .forms import BookingForm
from .models import Booking


@login_required
def create_booking(request, teacher_id):

    teacher = get_object_or_404(
        TeacherProfile,
        id=teacher_id,
        is_available=True
    )

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.student = request.user
            booking.teacher = teacher

            booking.save()

            return redirect('booking_success')

    else:
        form = BookingForm()

    context = {
        'teacher': teacher,
        'form': form,
    }

    return render(
        request,
        'booking.html',
        context
    )


def booking_success(request):

    return render(
        request,
        'booking-success.html'
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        student=request.user
    ).order_by('-booked_at')

    context = {
        'bookings': bookings
    }

    return render(
        request,
        'my-bookings.html',
        context
    )


@login_required
def student_booking_detail(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        student=request.user
    )

    return render(
        request,
        'booking-detail.html',
        {
            'booking': booking
        }
    )
@login_required
def booking_detail(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        teacher__user=request.user
    )

    return render(
        request,
        'booking-detail.html',
        {
            'booking': booking
        }
    )


@login_required
def update_booking_status(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        teacher__user=request.user
    )

    if request.method == 'POST':

        status = request.POST.get('status')

        if status == 'accepted':

            # Get lesson details from the teacher
            is_online = request.POST.get('is_online') == 'true'

            meeting_link = request.POST.get(
                'meeting_link',
                ''
            ).strip()

            location = request.POST.get(
                'location',
                ''
            ).strip()

            # Online lesson must have a meeting link
            if is_online and not meeting_link:
                return redirect(
                    'booking_detail',
                    booking_id=booking.id
                )

            # Offline lesson must have a location
            if not is_online and not location:
                return redirect(
                    'booking_detail',
                    booking_id=booking.id
                )

            booking.is_online = is_online
            booking.meeting_link = meeting_link
            booking.location = location
            booking.status = 'accepted'

            booking.save()

        elif status == 'cancelled':

            booking.status = 'cancelled'
            booking.save()

        elif status == 'completed':

            # Only an accepted booking can be completed
            if booking.status == 'accepted':

                booking.status = 'completed'
                booking.save()

    return redirect(
        'booking_detail',
        booking_id=booking.id
    )