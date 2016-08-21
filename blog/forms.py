import logging

from django import forms
from django.contrib.auth.models import User

from blog.models import Blog

class SignupForm(forms.ModelForm):
    blog_name = forms.CharField()

    def __init__(self, request, *args, **kwargs):
        blog_name = kwargs.get('blog_name')
        if blog_name:
            kwargs.pop('blog_name')
        super(SignupForm, self).__init__(*args, **kwargs)
        if blog_name:
            Blog.objects.create(name = blog_name, owner = request.user)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'blog_name')
