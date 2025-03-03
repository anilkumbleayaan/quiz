from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import get_user_model
from .models import QuizScore
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "quiz_app/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, "quiz_app/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, "quiz_app/register.html")

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Create Profile for the User
        Profile.objects.create(user=user, first_name=first_name, last_name=last_name)

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")  # Redirect to login page

    return render(request, "quiz_app/register.html")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        first_name = request.POST.get("first_name")  # New field
        last_name = request.POST.get("last_name")  # New field

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "quiz_app/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, "quiz_app/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return render(request, "quiz_app/register.html")

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Create profile and associate it with the user
        profile = Profile.objects.create(user=user, first_name=first_name, last_name=last_name, email=email)
        profile.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")

    return render(request, "quiz_app/register.html")
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from the form
        password = request.POST.get('password')

        # Get the User model
        User = get_user_model()

        try:
            user_obj = User.objects.get(email=email)  # Find user by email
            username = user_obj.username  # Get username from User object
        except User.DoesNotExist:
            username = None  # If no user found, authentication will fail

        if username:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('instruction')  # Redirect to instruction page
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "User with this email does not exist")

    return render(request, 'quiz_app/login.html')


@login_required
def instruction_view(request):
    return render(request, 'quiz_app/instruction.html')
def home_view(request):
    return render(request, 'quiz_app/index.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    
@login_required
def quiz_view(request):
    return render(request, 'quiz_app/quiz.html')  # Create this template


def system_compatibility_view(request):
    return render(request, 'quiz_app/system_compatibility.html')


def quiz_view(request):
    return render(request, "quiz_app/quiz.html")
@login_required
def submit_quiz(request):
    if request.method == "POST":
        user = request.user
        score = calculate_quiz_score(request)  # This function should already exist

        # Save score in the database
        QuizScore.objects.create(user=user, score=score)

    return None