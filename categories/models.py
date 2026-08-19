from django.db import models


class Category(models.Model):

    EDUCATION_LEVELS = (
        ('secondary', 'Secondary Education'),
        ('tertiary', 'Tertiary Education'),
    )

    name = models.CharField(
        max_length=100,
        unique=True
    )

    education_level = models.CharField(
        max_length=20,
        choices=EDUCATION_LEVELS,
        default='secondary'
    )

    def __str__(self):
        return self.name


class Subject(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    name = models.CharField(
        max_length=100
    )

    class Meta:
        unique_together = ('category', 'name')

    def __str__(self):
        return self.name