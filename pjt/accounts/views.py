from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm
)
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomAuthenticationForm, SetPasswordForm
from .models import User
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
            return redirect(request.GET.get('next') or 'http://127.0.0.1:8000/menu/')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signin.html', context)

def signup(request) :
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/menu/')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.nickname :
                pass
            else:
                user.nickname = user.username
                user.save()
            user.profile_image = 'image/user.jpg'
            user.save()
            auth_login(request, user)
            return redirect('http://127.0.0.1:8000/menu/')
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

# 감독 팔로우 기능
def follow(request, user_pk) :
    if request.user.is_authenticated:
        me = request.user
        you = get_object_or_404(get_user_model(), pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                isFollowed = False
            else:
                you.followers.add(me)
                isFollowed = True
            context = {
                'isFollowed': isFollowed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('behinds:index')
    return redirect('accounts:login')

# 유저 정보 삭제
def delete(request, user_pk) :
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('http://127.0.0.1:8000/')

# 유저 정보 수정
def update(request, user_pk) :
    user = User.objects.get(pk=request.user.pk)
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            form2 = SetPasswordForm(user, request.POST)
            if form2.is_valid():
                form2.save()
                update_session_auth_hash(request, form2.user)
                return redirect('mypage:index', user.pk)

            passwordForm = SetPasswordForm(user)
            form = CustomUserChangeForm(instance=user)
            auth_login(request, user)
            context = {
                'form': form,
                'passwordForm': passwordForm
            }   
            return render(request, 'accounts/update.html', context)
    else:
        passwordForm = SetPasswordForm(user)
        form = CustomUserChangeForm(instance=user)
        context = {
            'form': form,
            'passwordForm': passwordForm
        }
        return render(request, 'accounts/update.html', context)

def password(request) :
    pass
    return render(request, 'accounts/password.html')

