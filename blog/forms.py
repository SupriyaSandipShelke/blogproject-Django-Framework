from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write a clear, compelling title',
                'id': 'id_title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your story here...',
                'id': 'id_content'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'id_image_input'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
                'id': 'id_category'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'id_publish_toggle'
            }),
        }


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
