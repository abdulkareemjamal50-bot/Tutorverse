from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            'subject',
            'lesson_date',
            'lesson_time',
            'duration',
            'location',
            'is_online',
            'note',
        ]

        widgets = {
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter subject'
                }
            ),

            'lesson_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'lesson_time': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'time'
                }
            ),

            'duration': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 30,
                    'step': 30
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter lesson location'
                }
            ),

            'is_online': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),

            'note': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Any message for the tutor?'
                }
            ),
        }