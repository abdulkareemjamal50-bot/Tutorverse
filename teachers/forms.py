from django import forms
from django.contrib.auth import get_user_model

from .models import TeacherProfile


User = get_user_model()


class TeacherProfileForm(forms.ModelForm):

    # ==============================
    # USER INFORMATION
    # ==============================

    first_name = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }
        )
    )

    class Meta:
        model = TeacherProfile

        fields = [
            'first_name',
            'last_name',

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

            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Tell students about yourself and your teaching experience...'
                }
            ),

            'qualification': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'e.g. B.Sc. Mathematics'
                }
            ),

            'experience': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Years of teaching experience'
                }
            ),

            'hourly_rate': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your hourly rate'
                }
            ),

            'lesson_mode': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your city'
                }
            ),

            'state': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your state'
                }
            ),

            'latitude': forms.HiddenInput(),

            'longitude': forms.HiddenInput(),

            'profile_picture': forms.ClearableFileInput(
                attrs={
                    'accept': 'image/*'
                }
            ),

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

    # ==============================
    # LOAD USER NAME INTO FORM
    # ==============================

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)

        if self.user:

            self.fields['first_name'].initial = self.user.first_name

            self.fields['last_name'].initial = self.user.last_name