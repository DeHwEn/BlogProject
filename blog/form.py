from django import forms
from .models import Blog

class BlogPost(forms.ModelForm) :
    class Meta :
        model = Blog
        email = forms.EmailField()
        files = forms.FileField()
        fields = ['title', 'body']
        