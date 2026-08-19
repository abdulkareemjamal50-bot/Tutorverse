from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

from teachers.models import TeacherProfile


class StudentRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'

        if commit:
            user.save()

        return user


class TeacherRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'teacher'

        if commit:
            user.save()

            TeacherProfile.objects.create(
                user=user,
                bio='',
                qualification='',
                experience=0,
                hourly_rate=0,
                lesson_mode='online',
                city='',
                state=''
            )

        return user