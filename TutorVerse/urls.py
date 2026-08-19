from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'browse-teachers/',
        views.browse_teachers,
        name='browse_teachers'
    ),

    path(
        'teacher/<int:teacher_id>/',
        views.teacher_profile,
        name='teacher_profile'
    ),

    path(
        'bookings/',
        include('bookings.urls')
    ),
    path('accounts/', include('accounts.urls')),
    path(
    'student-profile/',
    views.student_profile,
    name='student_profile'
    ),
    path('teacher/', include('teachers.urls')),
    path(
    'messages/',
    include('messaging.urls')
),
path('contact/', views.contact, name='contact'),
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)