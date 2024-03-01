from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'login-register'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'login-register'}),
            'password1': forms.TextInput(attrs={'class': 'form-control', 'id': 'login-register'}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'id': 'login-register'}),

        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone', 'image']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'id': 'bio', 'rows': 4}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'id': 'image-input', 'onchange': 'previewImage(this)'})
        }
