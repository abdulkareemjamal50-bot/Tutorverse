from django import forms
from .models import StudentProfile


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile

        fields = [
            'profile_picture',
            'bio',
            'education_level',
            'city',
            'state',
        ]

        widgets = {

            'bio': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Tell us a little about yourself...'
            }),

            'education_level': forms.TextInput(attrs={
                'placeholder': 'e.g. Secondary School, University'
            }),

            'city': forms.TextInput(attrs={
                'placeholder': 'Your city'
            }),

            'state': forms.TextInput(attrs={
                'placeholder': 'Your state'
            }),
        }