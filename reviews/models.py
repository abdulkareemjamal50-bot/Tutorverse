from django.db import models
from django.conf import settings
from teachers.models import TeacherProfile
from bookings.models import Booking


class Review(models.Model):

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name='review',
        null=True,
        blank=True
    )

    rating = models.PositiveSmallIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.username} rated {self.teacher.user.username}"