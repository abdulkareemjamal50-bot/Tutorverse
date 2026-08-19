from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.contrib.auth.decorators import login_required

from teachers.models import TeacherProfile
from categories.models import Category, Subject

import math


# =========================
# HOME
# =========================

def home(request):
 categories = Category.objects.all()
 return render(
        request,
        'index.html',
        {
            'categories': categories
        }
    )


# =========================
# CALCULATE DISTANCE
# =========================

def calculate_distance(
    lat1,
    lon1,
    lat2,
    lon2
):

    earth_radius = 6371

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        +
        math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return earth_radius * c


# =========================
# BROWSE TEACHERS
# =========================

def browse_teachers(request):

    # =========================
    # GET SEARCH / FILTERS
    # =========================

    search = request.GET.get(
        'search',
        ''
    ).strip()

    category = request.GET.get(
        'category',
        ''
    ).strip()

    subject = request.GET.get(
        'subject',
        ''
    ).strip()

    lesson_mode = request.GET.get(
        'lesson_mode',
        ''
    ).strip()

    verified = request.GET.get(
        'verified',
        ''
    ).strip()


    # =========================
    # GET STUDENT LOCATION
    # =========================

    latitude = request.GET.get(
        'latitude'
    )

    longitude = request.GET.get(
        'longitude'
    )


    # =========================
    # GET AVAILABLE TEACHERS
    # =========================

    teachers = TeacherProfile.objects.filter(
        is_available=True
    ).prefetch_related(
        'subjects__category'
    )


    # =========================
    # SEARCH
    # =========================

    if search:

        teachers = teachers.filter(

            models.Q(
                user__first_name__icontains=search
            )

            |

            models.Q(
                user__last_name__icontains=search
            )

            |

            models.Q(
                user__username__icontains=search
            )

            |

            models.Q(
                subjects__name__icontains=search
            )

            |

            models.Q(
                subjects__category__name__icontains=search
            )

        ).distinct()


    # =========================
    # CATEGORY FILTER
    # =========================

    if category:

        teachers = teachers.filter(

            subjects__category__id=category

        ).distinct()


    # =========================
    # SUBJECT FILTER
    # =========================

    if subject:

        teachers = teachers.filter(

            subjects__id=subject

        ).distinct()


    # =========================
    # LESSON MODE FILTER
    # =========================

    if lesson_mode:

        teachers = teachers.filter(

            lesson_mode=lesson_mode

        )


    # =========================
    # VERIFIED FILTER
    # =========================

    if verified == '1':

        teachers = teachers.filter(

            verified=True

        )


    # =========================
    # GET CATEGORIES
    # =========================

    categories = Category.objects.all().order_by(
        'name'
    )


    # =========================
    # GET SUBJECTS
    # =========================

    subjects = Subject.objects.all().order_by(
        'name'
    )


    # =========================
    # STUDENT LOCATION
    # =========================

    try:

        student_lat = float(
            latitude
        )

        student_lon = float(
            longitude
        )

    except (
        TypeError,
        ValueError
    ):

        student_lat = None

        student_lon = None


    # =========================
    # CALCULATE TEACHER DISTANCE
    # =========================

    teacher_list = []


    for teacher in teachers:

        if (

            student_lat is not None

            and

            student_lon is not None

            and

            teacher.latitude is not None

            and

            teacher.longitude is not None

        ):

            distance = calculate_distance(

                student_lat,
                student_lon,

                teacher.latitude,
                teacher.longitude

            )

            teacher.distance = round(
                distance,
                1
            )

        else:

            teacher.distance = None


        teacher_list.append(
            teacher
        )


    # =========================
    # NEAREST TEACHERS FIRST
    # =========================

    if (

        student_lat is not None

        and

        student_lon is not None

    ):

        teacher_list.sort(

            key=lambda teacher:

            teacher.distance

            if teacher.distance is not None

            else float('inf')

        )


    # =========================
    # SEND DATA TO HTML
    # =========================

    context = {

        'teachers': teacher_list,

        'categories': categories,

        'subjects': subjects,

        'search': search,

        'selected_category': category,

        'selected_subject': subject,

        'selected_lesson_mode': lesson_mode,

        'verified': verified,

        'location_enabled': (

            student_lat is not None

            and

            student_lon is not None

        ),

    }


    return render(

        request,

        'browse-teachers.html',

        context

    )


# =========================
# ABOUT
# =========================

def about(request):

    return render(
        request,
        'about.html'
    )


# =========================
# TEACHER PROFILE
# =========================

def teacher_profile(
    request,
    teacher_id
):

    teacher = get_object_or_404(

        TeacherProfile,

        id=teacher_id

    )


    context = {

        'teacher': teacher

    }


    return render(

        request,

        'teachers-pro.html',

        context

    )


# =========================
# STUDENT PROFILE
# =========================

@login_required
def student_profile(request):

    return render(

        request,

        'student-profile.html',

        {
            'user': request.user
        }

    )


def contact(request):
    return render(request, 'contact.html')