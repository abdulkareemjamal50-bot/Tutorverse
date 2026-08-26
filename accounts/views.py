import json

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from pathlib import Path

from django.conf import settings
import firebase_admin
from firebase_admin import credentials, auth as firebase_auth



from .forms import StudentRegistrationForm, TeacherRegistrationForm


# ============================================================
# FIREBASE INITIALIZATION
# ============================================================

# IMPORTANT:
# We will configure the Firebase service-account file separately.
# Do NOT put the service-account private key directly in this file.

if not firebase_admin._apps:

    firebase_credentials = (
        settings.BASE_DIR /
        "firebase-service-account.json"
    )

    cred = credentials.Certificate(
        str(firebase_credentials)
    )

    firebase_admin.initialize_app(cred)

# ============================================================
# REGISTER
# ============================================================

def register(request):
    return render(request, 'accounts/register.html')


# ============================================================
# STUDENT REGISTRATION
# ============================================================

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


# ============================================================
# TEACHER REGISTRATION
# ============================================================

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


# ============================================================
# NORMAL DJANGO LOGIN
# ============================================================

def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

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


# ============================================================
# FIREBASE GOOGLE LOGIN
# ============================================================

def firebase_login(request):

    if request.method != 'POST':

        return JsonResponse({
            'success': False,
            'error': 'POST request required.'
        }, status=405)


    try:

        # ----------------------------------------------------
        # Get JSON sent from Firebase JavaScript
        # ----------------------------------------------------

        data = json.loads(request.body)

        id_token = data.get('idToken')


        if not id_token:

            return JsonResponse({
                'success': False,
                'error': 'Firebase ID token is missing.'
            }, status=400)


        # ----------------------------------------------------
        # Verify Firebase ID token
        # ----------------------------------------------------

        decoded_token = firebase_auth.verify_id_token(
            id_token
        )


        # ----------------------------------------------------
        # Get Firebase user information
        # ----------------------------------------------------

        firebase_uid = decoded_token.get('uid')

        email = decoded_token.get('email')

        name = decoded_token.get('name', '')

        picture = decoded_token.get('picture', '')


        if not email:

            return JsonResponse({
                'success': False,
                'error': 'Google account does not have an email address.'
            }, status=400)


        # ----------------------------------------------------
        # Find existing Django user
        # ----------------------------------------------------

        from django.contrib.auth import get_user_model

        User = get_user_model()

        user = User.objects.filter(
            email__iexact=email
        ).first()


        # ----------------------------------------------------
        # Create Django user if they don't exist
        # ----------------------------------------------------

        if user is None:

            # Use email as username if your User model
            # still uses Django's username field.

            username = email.split('@')[0]

            # Make username unique
            original_username = username
            counter = 1

            while User.objects.filter(
                username=username
            ).exists():

                username = (
                    f"{original_username}{counter}"
                )

                counter += 1


            user = User.objects.create_user(

                username=username,

                email=email,

                first_name=name.split(' ')[0]
                if name else '',

            )

            # Google-created users should not have
            # a normal password login.

            user.set_unusable_password()

            user.save()


        # ----------------------------------------------------
        # Log Django user in
        # ----------------------------------------------------

        login(request, user)


        # ----------------------------------------------------
        # Decide where the user should go
        # ----------------------------------------------------

        if hasattr(user, 'role'):

            if user.role == 'teacher':

                redirect_url = '/teacher/dashboard/'

            elif user.role == 'student':

                redirect_url = '/student/dashboard/'

            else:

                redirect_url = '/'

        else:

            redirect_url = '/'


        return JsonResponse({

            'success': True,

            'redirect_url': redirect_url,

            'email': user.email,

            'name': (
                user.get_full_name()
                or user.username
            )

        })


    except firebase_auth.InvalidIdTokenError:

        return JsonResponse({

            'success': False,

            'error': 'Invalid Firebase ID token.'

        }, status=401)


    except firebase_auth.ExpiredIdTokenError:

        return JsonResponse({

            'success': False,

            'error': 'Firebase ID token has expired. Please sign in again.'

        }, status=401)


    except Exception as e:

        print("Firebase login error:", e)

        return JsonResponse({

            'success': False,

            'error': 'Google Sign-In could not be completed.'

        }, status=500)


# ============================================================
# LOGOUT
# ============================================================

def logout_view(request):

    logout(request)

    return redirect('/')