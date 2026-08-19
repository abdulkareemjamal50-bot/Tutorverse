from django.db import models
from django.conf import settings


class Course(models.Model):

    LEVELS = (
        ('secondary', 'Secondary Education'),
        ('tertiary', 'Tertiary Education'),
    )

    teacher = models.ForeignKey(
        'teachers.TeacherProfile',
        on_delete=models.CASCADE,
        related_name='courses'
    )

    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name='courses'
    )

    subject = models.ForeignKey(
        'categories.Subject',
        on_delete=models.CASCADE,
        related_name='courses'
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    education_level = models.CharField(
        max_length=20,
        choices=LEVELS
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    duration = models.CharField(
        max_length=100,
        blank=True
    )

    course_image = models.ImageField(
        upload_to='courses/',
        blank=True,
        null=True
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title