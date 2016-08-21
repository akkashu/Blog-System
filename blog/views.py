from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from blog.models import Blog, Article, Comment
from blog.forms import SignupForm

class SignupView(View):

    def get(self, request, *args, **kwargs):
        form = SignupForm(request) 
        return render_to_response('blog/signup.html',
                {
                    'form': form,
                })

    def post(self, request, *args, **kwargs):
        pass

def login(request, *args, **kwargs):
    pass

def article_list_view(request, *args, **kwargs):
    pass

def article_detail_view(request, *args, **kwargs):
    pass

def blog_view(request, *args, **kwargs):
    pass
