from django.db import models
from django.conf import settings
from teachers.models import TeacherProfile


class Booking(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_bookings"
    )

    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name="teacher_bookings"
    )

    subject = models.CharField(max_length=150)

    lesson_date = models.DateField()

    lesson_time = models.TimeField()

    duration = models.PositiveIntegerField(
        default=60,
        help_text="Duration in minutes"
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    is_online = models.BooleanField(default=True)

    note = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} booked {self.teacher.user.username}"
