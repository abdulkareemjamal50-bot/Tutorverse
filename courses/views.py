from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import CourseForm
from teachers.models import TeacherProfile


def course_list(request):

    courses = Course.objects.filter(
        is_available=True
    ).select_related(
        'teacher__user',
        'category',
        'subject'
    )

    context = {
        'courses': courses,
    }

    return render(
        request,
        'courses/course_list.html',
        context
    )


def course_detail(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id,
        is_available=True
    )

    context = {
        'course': course,
    }

    return render(
        request,
        'courses/course_detail.html',
        context
    )


@login_required
def create_course(request):

    teacher = get_object_or_404(
        TeacherProfile,
        user=request.user
    )

    if request.method == 'POST':

        form = CourseForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            course = form.save(commit=False)

            course.teacher = teacher

            course.save()

            return redirect('teacher_dashboard')

    else:

        form = CourseForm()

    return render(
        request,
        'courses/create_course.html',
        {
            'form': form
        }
    )