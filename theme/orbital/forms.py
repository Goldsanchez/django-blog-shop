from django import forms
from django.forms import ModelForm
from .models import New, Comment

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'
        widgets = {'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Write your new'}),
                   'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your new'}),
                   'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Write your new'}),
                   'detail': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your new'}),}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your name'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Write your email'}),
                   'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment'}),}