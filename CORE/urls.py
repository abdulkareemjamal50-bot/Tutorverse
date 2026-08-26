from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    # Main Tutorverse pages
    path('', include('TutorVerse.urls')),

    # Authentication
    path('accounts/', include('accounts.urls')),

    # Student dashboard
    path('student/', include('student_dashboard.urls')),

    # Teacher dashboard
    path('teacher-dashboard/', include('teacher_dashboard.urls')),

    # Teachers
    path('teachers/', include('teachers.urls')),

    # Courses
    path('courses/', include('courses.urls')),
    path(
    'blog/',
    include('blog.urls')
),
    
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )