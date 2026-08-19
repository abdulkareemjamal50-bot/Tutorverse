from django.urls import path
from . import views

urlpatterns = [

    path(
        'student/register/',
        views.student_register,
        name='student_register'
    ),

    path(
        'teacher/register/',
        views.teacher_register,
        name='teacher_register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
    path(
    'register/',
    views.register,
    name='register'
),
]