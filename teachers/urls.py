from django.urls import path
from . import views


urlpatterns = [

    path(
        'profile/setup/',
        views.teacher_profile_setup,
        name='teacher_profile_setup'
    ),

    path(
        '<int:teacher_id>/',
        views.teacher_detail,
        name='teacher_detail'
    ),

]