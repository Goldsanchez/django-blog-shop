from django import forms
from django.contrib.auth import login
from django.forms import ModelForm
from django.forms.widgets import PasswordInput
from .models import New, Comment

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, UserManager




class NewForm(ModelForm):
    class Meta:
        model = New
        fields = '__all__'
        widgets = {'category': forms.Select(attrs={'class': 'form-control'}),
                   'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title'}),
                   'image': forms.FileInput(attrs={'class': 'form-control-file'}),
                   'detail': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your new'}),}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your name'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Write your email'}),
                   'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment'}),}
