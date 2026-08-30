from django.db import models
from django.conf import settings


class TeacherProfile(models.Model):

    LESSON_MODE = (
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('both', 'Both'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    subjects = models.ManyToManyField(
        'categories.Subject',
        related_name='teachers'
    )

    bio = models.TextField()

    qualification = models.CharField(
        max_length=200
    )

    experience = models.PositiveIntegerField(
        help_text="Years of teaching experience"
    )

    hourly_rate = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    lesson_mode = models.CharField(
        max_length=10,
        choices=LESSON_MODE,
        default='online'
    )

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    latitude = models.FloatField(
        null=True,
        blank=True
    )

    longitude = models.FloatField(
        null=True,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to='teachers/',
        blank=True,
        null=True
    )

    intro_video = models.FileField(
        upload_to='teacher_videos/',
        blank=True,
        null=True
    )

    # =========================================
    # IDENTITY VERIFICATION
    # =========================================

    identity_document = models.FileField(
        upload_to='teacher_identity_documents/',
        blank=True,
        null=True,
        help_text="Upload a valid government-issued ID."
    )

    identity_document_type = models.CharField(
        max_length=50,
        blank=True,
        choices=(
            ('national_id', 'National ID'),
            ('drivers_license', "Driver's License"),
            ('passport', 'International Passport'),
            ('voters_card', "Voter's Card"),
            ('other', 'Other'),
        )
    )

    verified = models.BooleanField(
        default=False
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username