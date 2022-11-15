from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    PasswordChangeForm
)
# Create your views here.

def index(request) :
    pass
    return render(request, 'accounts/index.html')
    
def login(request):
    if request.user.is_authenticated:
        return redirect('behinds:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'behinds:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request) :
    pass
    return render(request, 'accounts/logout.html')

def signup(request) :
    pass
    return render(request, 'accounts/signup.html')

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