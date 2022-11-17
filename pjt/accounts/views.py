from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm
)
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomAuthenticationForm
# Create your views here.

def index(request) :
    pass
    return render(request, 'accounts/index.html')
    
def signin(request):
    if request.user.is_authenticated:
        return redirect('behinds:index')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'behinds:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signin.html', context)

def signup(request) :
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user.nickname)
            if user.nickname :
                pass
            else:
                user.nickname = user.username
                user.save()
            auth_login(request, user)
            return redirect('behinds:index')
        form = CustomUserCreationForm()
        context = {
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('http://127.0.0.1:8000/')

def password(request) :
    pass
    return render(request, 'accounts/password.html')

def profile(request) :
    pass
    return render(request, 'accounts/profile.html')

def update(request) :
    pass
    return render(request, 'accounts/update.html')

def delete(request) :
    pass
    return render(request, 'accounts/delete.html')

def follow(request) :
    pass
    return render(request, 'accounts/follow.html')