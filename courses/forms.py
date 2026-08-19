from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course

        fields = [
            'category',
            'subject',
            'title',
            'description',
            'education_level',
            'price',
            'duration',
            'course_image',
            'is_available',
        ]

        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 5
            }),

            'education_level': forms.Select(),

            'is_available': forms.CheckboxInput(),
        }