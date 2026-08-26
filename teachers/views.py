from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import TeacherProfile
from .forms import TeacherProfileForm


@login_required
def teacher_profile_setup(request):

    profile, created = TeacherProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        form = TeacherProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect('teacher_dashboard')

    else:

        form = TeacherProfileForm(
            instance=profile
        )

    return render(
        request,
        'teachers/profile_setup.html',
        {
            'form': form
        }
    )


@login_required
def teacher_detail(request, teacher_id):

    teacher = get_object_or_404(
        TeacherProfile,
        id=teacher_id
    )

    return render(
        request,
        'teachers/teacher_detail.html',
        {
            'teacher': teacher
        }
    )


@login_required
def teacher_student_profile(request, student_id):

    student = get_object_or_404(
        User,
        id=student_id
    )

    return render(
        request,
        'teachers/student_profile.html',
        {
            'student': student
        }
    )