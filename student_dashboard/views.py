from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bookings.models import Booking
from .models import StudentProfile
from .forms import StudentProfileForm

from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404


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


# ==========================================
# STUDENT PROFILE
# ==========================================

@login_required
def student_profile(request):

    profile, created = StudentProfile.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        'student_dashboard/student_profile.html',
        {
            'profile': profile,
        }
    )


# ==========================================
# EDIT STUDENT PROFILE
# ==========================================

@login_required
def edit_student_profile(request):

    profile, created = StudentProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('student_profile')

    else:

        form = StudentProfileForm(
            instance=profile
        )

    return render(
        request,
        'student_dashboard/edit_student_profile.html',
        {
            'form': form,
            'profile': profile,
        }
    )
# ==========================================
# TEACHER VIEW STUDENT PROFILE
# ==========================================

@login_required
def teacher_view_student_profile(request, student_id):

    student = get_object_or_404(
        settings.AUTH_USER_MODEL,
        id=student_id
    )

    profile, created = StudentProfile.objects.get_or_create(
        user=student
    )

    return render(
        request,
        'student_dashboard/student_profile.html',
        {
            'profile': profile,
            'student': student,
        }
    )