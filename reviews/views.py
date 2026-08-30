from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from bookings.models import Booking
from .models import Review
from .forms import ReviewForm


@login_required
def create_review(request, booking_id):

    # Only the student who made the booking
    # can review it, and only after completion.
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        student=request.user,
        status='completed'
    )

    # Prevent the same booking from being reviewed twice
    existing_review = Review.objects.filter(
        booking=booking
    ).first()

    if existing_review:
        return redirect(
            'student_booking_detail',
            booking_id=booking.id
        )

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():

            review = form.save(commit=False)

            review.student = request.user
            review.teacher = booking.teacher
            review.booking = booking

            review.save()

            return redirect(
                'student_booking_detail',
                booking_id=booking.id
            )

    else:

        form = ReviewForm()

    context = {
        'booking': booking,
        'form': form,
    }

    return render(
        request,
        'reviews/create_review.html',
        context
    )