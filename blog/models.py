from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):

    CATEGORY_CHOICES = [
        ('Study Tips', 'Study Tips'),
        ('Education', 'Education'),
        ('Online Learning', 'Online Learning'),
        ('Tutoring', 'Tutoring'),
        ('Exams', 'Exams'),
        ('Career', 'Career'),
    ]

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Education'
    )

    image = models.ImageField(
        upload_to='blog/',
        blank=True,
        null=True
    )

    excerpt = models.TextField(
        max_length=300,
        help_text='Short description shown on the blog card.'
    )

    content = models.TextField(
        help_text='Full article content.'
    )

    author = models.CharField(
        max_length=100,
        default='Tutorverse'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    published = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
