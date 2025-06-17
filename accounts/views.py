from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)

        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rpassword = request.POST.get('rpassword')

        if password == rpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'There exists an account with this email')
                return redirect('signup')
            elif User.objects.filter(username=username):
                messages.error(request, 'Username already in use')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

    return render(request, 'accounts/signup.html')

@login_required
def complete_profile(request):
    directorates = Directorate.objects.all()
    profile = request.user.memberprofile
    
    context = {
        'directorates' : directorates
    }

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        contact = request.POST.get('contact')
        directorate_id = request.POST.get('directorate')

        request.user.first_name = fname
        request.user.last_name = lname
        request.user.save()

        profile.phone_number = contact
        profile.directorate_id = directorate_id
        profile.save()

        return redirect('home')

    return render(request, 'accounts/complete_profile.html', context)

def view_profile(request):

    profile = request.user.memberprofile

    context = {
        'user': request.user,
        'profile': profile,
    }

    return render(request, 'accounts/view_profile.html', context)