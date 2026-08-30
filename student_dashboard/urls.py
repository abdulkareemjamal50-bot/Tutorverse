from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.dashboard,
        name='student_dashboard'
    ),

    path(
        'profile/',
        views.student_profile,
        name='student_profile'
    ),

    path(
        'profile/edit/',
        views.edit_student_profile,
        name='edit_student_profile'
    ),
    path(
    'student/<int:student_id>/',
    views.teacher_view_student_profile,
    name='teacher_view_student_profile'
),

]