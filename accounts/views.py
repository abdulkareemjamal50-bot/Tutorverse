from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import StudentRegistrationForm, TeacherRegistrationForm

def register(request):
    return render(request, 'accounts/register.html')
# Student Registration
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_dashboard')

    else:
        form = StudentRegistrationForm()

    return render(request, 'accounts/student_register.html', {
        'form': form
    })


# Teacher Registration
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('teacher_dashboard')

    else:
        form = TeacherRegistrationForm()

    return render(request, 'accounts/teacher_register.html', {
        'form': form
    })


# Login
def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            if user.role == 'teacher':
                return redirect('teacher_dashboard')

            elif user.role == 'student':
                return redirect('student_dashboard')

            return redirect('/')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {
        'form': form
    })


# Logout
def logout_view(request):
    logout(request)
    return redirect('/')
