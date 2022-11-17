from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'nickname')

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(
        max_length=200,
        required = True,
        help_text='Enter Username',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
            }
        ),
    )

    nickname = forms.CharField(
        max_length=200,
        required = True,
        help_text='Enter Username',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
            }
        ),
        required = False,
        help_text='Enter Nickname',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '입력하지 않으면 username으로 자동생성 되며 추후 개인 정보에서 수정 가능합니다.'}),
    )

    email = forms.EmailField(
        max_length=100,
        required = True,
        help_text='Enter Email Address',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
            }
        ),
    )
    password1 = forms.CharField(
        help_text='Enter password',
        required = True,
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control', 
                'style': 'width: 90%;' 'height: 40px;' 'border: none;' 'border-radius: 10px;' 'background-color: #D9D9D9;' 'font-family: login;' 'padding-left: 10px;',
            }
        ),
    )
    password2 = None

    class Meta:
        model = get_user_model()
        fields = [
        'username', 'nickname', 'email', 'password1',
        ]