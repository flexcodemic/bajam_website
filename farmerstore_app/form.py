from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        field = ['username', 'email', 'password1', 'password2']

    class UserLoginForm(AuthenticationForm):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)