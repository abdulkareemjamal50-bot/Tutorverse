from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review

        fields = [
            'rating',
            'comment',
        ]

        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Tell us about your experience with this tutor...'
                }
            ),
        }

        labels = {
            'rating': 'Your Rating',
            'comment': 'Your Review',
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')

        if not rating:
            raise forms.ValidationError(
                'Please select a rating.'
            )

        if rating < 1 or rating > 5:
            raise forms.ValidationError(
                'Rating must be between 1 and 5 stars.'
            )

        return rating