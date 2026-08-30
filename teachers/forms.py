from django import forms
from .models import TeacherProfile


class TeacherProfileForm(forms.ModelForm):

    class Meta:
        model = TeacherProfile

        fields = [
            'subjects',
            'bio',
            'qualification',
            'experience',
            'hourly_rate',
            'lesson_mode',
            'city',
            'state',
            'latitude',
            'longitude',
            'profile_picture',
            'intro_video',

            # IDENTITY VERIFICATION
            'identity_document_type',
            'identity_document',
        ]

        widgets = {

            'subjects': forms.CheckboxSelectMultiple(),

            'latitude': forms.HiddenInput(),

            'longitude': forms.HiddenInput(),

            'intro_video': forms.ClearableFileInput(
                attrs={
                    'accept': 'video/*'
                }
            ),

            'identity_document_type': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'identity_document': forms.ClearableFileInput(
                attrs={
                    'accept': '.pdf,.jpg,.jpeg,.png'
                }
            ),
        }