from django import forms

from .models import Post

class PostForm(form.ModelForm):
    