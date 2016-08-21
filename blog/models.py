from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    name = models.CharField(max_length = 100)
    owner = models.ForeignKey(User, related_name = "blogs")

class Article(models.Model):
    blog = models.ForeignKey(Blog, related_name = "articles")
    created = models.DateTimeField(auto_now = True)
    modified = models.DateTimeField(auto_now_add = True) 
    title = models.CharField(max_length=200)
    body = models.CharField(max_length = 10000)
    author = models.ForeignKey(User, related_name = "articles")

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name = "comments")
    comment = models.CharField(max_length = 1000)
    created = models.DateTimeField(auto_now = True)
    commentor = models.ForeignKey(User, related_name = "comments")
