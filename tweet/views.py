from dataclasses import field
from multiprocessing import context
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post

class PostlListView(ListView):
    model = Post
    template_name = "tweet/index.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    pagenate_by = 5


class PostCreateView(CreateView):
    model = Post
    fields = ['content'] #投稿するときに何を使うのか
    template_name = 'tweet/post_create.html'
    success_url = '/'